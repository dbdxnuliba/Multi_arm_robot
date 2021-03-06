//id1-7位置控制，id8-14阻抗控制
#include "ros/ros.h"
#include "std_msgs/Float64MultiArray.h"
#include "std_msgs/Float32.h"
#include "sensor_msgs/JointState.h"
#include <sstream>
#include <stdio.h>
#include "force_sensor/global.h"                                                     //自定义全局变量
#include <math.h>
//全局变量
float force1[6] = {0};
float force2[6] = {0};
float g_Trans_Output_last = 0, g_Trans_Output_last2 = 0, g_Trans_Input_last = 0, g_Trans_Input_last2 = 0, deltaz = 0;    //阻抗控制中修改的量
void forceCallback1(const std_msgs::Float64MultiArray::ConstPtr& msg){              //id1-7的力传感器
    force1[0] = static_cast<float>(msg->data[0]);
    force1[1] = static_cast<float>(msg->data[1]);
    force1[2] = static_cast<float>(msg->data[2]);
    force1[3] = static_cast<float>(msg->data[3]);
    force1[4] = static_cast<float>(msg->data[4]);
    force1[5] = static_cast<float>(msg->data[5]);
}

void forceCallback2(const std_msgs::Float64MultiArray::ConstPtr& msg){              //id8-14的力传感器
    force2[0] = static_cast<float>(msg->data[0]);
    force2[1] = static_cast<float>(msg->data[1]);
    force2[2] = static_cast<float>(msg->data[2]);
    force2[3] = static_cast<float>(msg->data[3]);
    force2[4] = static_cast<float>(msg->data[4]);
    force2[5] = static_cast<float>(msg->data[5]);
    ROS_INFO("force2:%f",force2[2]);
}

float DifferenceEquation(float Md, float Bd, float Kd,float deltafz){               //阻抗差分方，单方向
    float deltaz;
    float w1,w2,w3;
    float T = 0.02;                                                                 //控制周期50Hz
    w1 = 4*Md + 2*Bd*T + Kd*T*T;                                                    //南皮书相关
    w2 = -8*Md + 2*Kd*T*T;
    w3 = 4*Md - 2*Bd*T + Kd*T*T;
    deltaz = T*T/w1*(deltafz + 2*g_Trans_Input_last + g_Trans_Input_last2) - w2/w1*(g_Trans_Output_last) - w3/w1*(g_Trans_Output_last2);
    g_Trans_Output_last2 = g_Trans_Output_last;                                     //记录两次力和两次误差
    g_Trans_Output_last = deltaz;
    g_Trans_Input_last2 = g_Trans_Input_last;
    g_Trans_Input_last = deltafz;
    return deltaz;
}

float Desired_force(float t){                                                      //期望力基本为一个定值
    float F;
    if(t <= 5)
        F = 0;
    else if(t > 5 && t <= 35)
        F = 20;                                                                    //双臂的接触力，需要修改
    return F;
}

void Pose_mod(float T[4][4], float deltaZ, float T0e[4][4]){                       //位姿修正
    deltaz = deltaz + deltaZ;
    T[2][3] = T[2][3] + deltaz;
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            T0e[i][j] = T[i][j];
}

int main(int argc, char **argv){
    ros::init(argc, argv, "dualarm_impedence_control");
    ros::NodeHandle nh;
    ros::Publisher pos_pub = nh.advertise<sensor_msgs::JointState>("/joint_command",1000);    //发送命令
    ros::Subscriber force_sub1 = nh.subscribe("six_axis_force_1",1000,forceCallback1);
    ros::Subscriber force_sub2 = nh.subscribe("six_axis_force_2",1000,forceCallback2);
    ros::Rate loop_rate(50);
    float M = 1;
    float B = 600;
    float K = 90000;   //阻抗参数，需要修改
    float theta00[7] = {140,240,180,260,180,220,50};    //id1-7的逆解迭代初始角度
    float theta01[7] = {220,120,180,100,180,140,40};    //id8-14的逆解迭代初始角度
    float thetat0[7] = {0};
    float thetat1[7] = {0};
    float Toa_ea[4][4], Tob_eb[4][4],T0e[4][4];
    float tt = 0;
    float deltafz,deltaz_mod;
    int time = 1;
    usleep(2000000);    //2s
    sensor_msgs::JointState jointCommand;
    for(int i = 0; i < 14; i++)
        jointCommand.position.push_back(0);
    while(ros::ok && tt <= 35){
    // while(ros::ok && tt <= 8){
        // if(sqrt(force1[1]*force1[1] + force1[2]*force1[2]) > 20){
        //     ROS_INFO("force detected,stop!");
        // }

        PathPlanning(tt,Toa_ea,Tob_eb); //规划末端位姿
        My_ikine_IteraFcn(Toa_ea,theta00,thetat0);  //id1-7关节角度
        
        deltafz = -force2[2] - Desired_force(tt);
        deltaz_mod = DifferenceEquation(M,B,K,deltafz);  //阻抗控制的修正量
        ROS_INFO("%d deltaf:%.4f  deltaz:%.4f",time++,deltafz,deltaz_mod);
        Pose_mod(Tob_eb,deltaz_mod,T0e);    //修正量与规划量叠加
        My_ikine_IteraFcn(T0e,theta01,thetat1);  //id8-14关节角度
        tt = tt + 0.02;
        //ID 1-7
        jointCommand.position[0] = thetat0[0] + 2;  //ID1
        jointCommand.position[1] = thetat0[1] + 1;  //ID2
        jointCommand.position[2] = thetat0[2];  //ID3
        jointCommand.position[3] = thetat0[3] + 2;  //ID4
        jointCommand.position[4] = thetat0[4];  //ID5
        jointCommand.position[5] = thetat0[5] + 1;  //ID6
        jointCommand.position[6] = thetat0[6];  //ID7
        //ID 8-14
        jointCommand.position[7] = thetat1[0] + 2;  //ID8
        jointCommand.position[8] = thetat1[1];  //ID9
        jointCommand.position[9] = thetat1[2] + 2;  //ID10
        jointCommand.position[10] = thetat1[3] - 2;  //ID11
        jointCommand.position[11] = thetat1[4];  //ID12
        jointCommand.position[12] = thetat1[5];  //ID13
        jointCommand.position[13] = thetat1[6];  //ID14

        if(Judge_joint_outof_angle(thetat0,thetat1) == 1)   //判断逆解是否超过关节极限
            break;
        pos_pub.publish(jointCommand);
        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}

//simulation
// int main(int argc, char **argv){
//     ros::init(argc, argv, "dualarm_impedence_control_simulation");
//     ros::NodeHandle nh;
//     ros::Publisher pos_pub = nh.advertise<sensor_msgs::JointState>("/joint_command",1000);
//     ros::Publisher force_pub = nh.advertise<std_msgs::Float32>("/force1",100);
//     ros::Rate loop_rate(50);
//     float M = 1;
//     float B = 200;
//     float K = 40000;
//     float theta00[7] = {140,240,180,260,180,220,50};    //id1-7的逆解迭代初始角度
//     float theta01[7] = {220,120,180,100,180,140,40};    //id8-14的逆解迭代初始角度
//     float thetat0[7] = {0};
//     float thetat1[7] = {0};
//     float Toa_ea[4][4], Tob_eb[4][4], T0e[4][4], TB_L_tt[4][4];
//     float tt = 0;
//     float deltafz,deltaz_mod = 0;
//     int time = 1;
//     usleep(5000000);    //5s
//     sensor_msgs::JointState jointCommand;
//     std_msgs::Float32 force1;
//     for(int i = 0; i < 14; i++)
//         jointCommand.position.push_back(0);
//     while(ros::ok && tt <= 33){
//         PathPlanningSim(tt,Toa_ea,TB_L_tt,Tob_eb); //规划末端位姿
//         My_ikine_IteraFcn(Toa_ea,theta00,thetat0);  //id1-7关节角度
//         if(tt == 0){
//             My_ikine_IteraFcn(Tob_eb,theta01,thetat1);
//             Pose_mod(Tob_eb,deltaz_mod,T0e);
//         }
//         else{
//             deltafz = EnvironmentForce(T0e,TB_L_tt,tt);
//             force1.data = deltafz;
//             force_pub.publish(force1);
//             ROS_INFO("%f",deltafz);
//             deltaz_mod = DifferenceEquation(M,B,K,deltafz);  //阻抗控制的修正量
//             Pose_mod(Tob_eb,deltaz_mod,T0e);    //修正量与规划量叠加
//             My_ikine_IteraFcn(T0e,theta01,thetat1);  //id8-14关节角度
//         }
//         tt = tt + 0.02;
//         for(int i = 0; i < 7; i++)
//             jointCommand.position[i] = thetat0[i];
//         for(int i = 0; i < 7; i++)
//             jointCommand.position[i+7] = thetat1[i];
//         if(Judge_joint_outof_angle(thetat0,thetat1) == 1)   //判断逆解是否超过关节极限
//             break;
//         // ROS_INFO("%d",time++);
//         pos_pub.publish(jointCommand);
//         loop_rate.sleep();
//     }
//     return 0;
// }
