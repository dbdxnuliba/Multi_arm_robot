/*joint_command_transfer.cpp
 *上位级与下位机转接接口
 *
 * */
#include "ros/ros.h"
#include "testcan/IpPos.h"
#include "iostream"
#include "fstream"
#include "sensor_msgs/JointState.h"
#include "std_msgs/Bool.h"
#include "std_msgs/Float64MultiArray.h"
#define postoangle 1440000.0/360 
#define big 2498560.0/360
#define small 1440000.0/360
#define degreetoradius 180.0/3.1415926
#define radiustodegree 3.1415926/180.0

using namespace std;
class JointCommand{
public:
    JointCommand();
    void registerNodeHandle(ros::NodeHandle& _nh);
    void registerPubSub();
    void fCallback1(const std_msgs::Bool::ConstPtr& resetCommandMsg);
    void fCallback2(const std_msgs::Float64MultiArray::ConstPtr& jointCommandMsg);
private:
    int count_reset = 0;
    int resetFlag = 1;
    int count_receive = 0;
    double jointPosition[7];
    double jointPositionInEncoder[7];

    testcan::IpPos ip_pos;
    ros::Publisher pos_pub;
    ros::Subscriber resetCommandSub;
    ros::Subscriber jointCommandSub;
    ros::NodeHandle nh;
};

int main(int argc, char *argv[])
{
    printf("hello\n");
    ros::init(argc, argv, "joint_command_transfer_node");
    ros::NodeHandle nh;
     
    JointCommand JointCommand1;

    JointCommand1.registerNodeHandle(nh);
    JointCommand1.registerPubSub();
    
    ros::spin();

    return 0;
}
JointCommand::JointCommand(){}

void JointCommand::registerNodeHandle(ros::NodeHandle& _nh){
    nh = _nh;
}

void JointCommand::registerPubSub(){
    //将数据发送到底层节点
    pos_pub = nh.advertise<testcan::IpPos>("/canopenexample/ip_pos",8);

    //订阅上位及关节命令
    //resetCommandSub = nh.subscribe("/reset_flag",2,&JointCommand::fCallback1, this);
    jointCommandSub = nh.subscribe("/armt/joint_command",40,&JointCommand::fCallback2, this);
}

void JointCommand::fCallback1(const std_msgs::Bool::ConstPtr& resetCommandMsg){
    count_reset++;
    if (count_reset == 50)
    {
        ROS_INFO("got a  Reset");
        count_reset = 0;
    }
    if(resetCommandMsg->data)
        resetFlag = 1;
}

//接收上位机Float64数组
void JointCommand::fCallback2(const std_msgs::Float64MultiArray::ConstPtr& jointCommandMsg){
    //count_receive++;                                                                       //接受计数加1
    for(int i=0;i<7;i++)
    {
        jointPositionInEncoder[i] = degreetoradius * jointCommandMsg->data[i];             //弧度单位转为角度单位
    }
    if(count_receive == 50)
    {
        ROS_INFO("recive:%.3f %.3f %.3f %.3f %.3f %.3f %.3f",jointPositionInEncoder[0],
        jointPositionInEncoder[1],jointPositionInEncoder[2],jointPositionInEncoder[3],jointPositionInEncoder[4],jointPositionInEncoder[5],jointPositionInEncoder[6]);
        count_receive = 0;
    }
    if(!resetFlag){
            ROS_INFO("Wait For Reset");
        }
    else{
        for(int i = 0; i < 7; i++) //分别向关节发送关节角度
        {
            ip_pos.id = i+1;
            ip_pos.pos = jointPositionInEncoder[i];
            pos_pub.publish(ip_pos);
            //ROS_INFO("send motor %d  a angle of %f",i+1,jointPositionInEncoder[i]);
        }
    }
}
