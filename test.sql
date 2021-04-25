/*
Navicat MySQL Data Transfer

Source Server         : 本地数据库
Source Server Version : 80021
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 80021
File Encoding         : 65001

Date: 2021-04-24 22:57:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for childrenmenus
-- ----------------------------
DROP TABLE IF EXISTS `childrenmenus`;
CREATE TABLE `childrenmenus` (
  `psc_id` int NOT NULL AUTO_INCREMENT,
  `ps_name` varchar(20) NOT NULL,
  `ps_pid` int NOT NULL,
  `ps_path` varchar(20) NOT NULL,
  `ps_level` enum('3','1','2') NOT NULL,
  PRIMARY KEY (`psc_id`),
  KEY `ix_childrenmenus_ps_pid` (`ps_pid`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of childrenmenus
-- ----------------------------
INSERT INTO `childrenmenus` VALUES ('1', '宿舍信息', '101', 'dormitory', '1');
INSERT INTO `childrenmenus` VALUES ('2', '学生信息', '102', 'message', '1');
INSERT INTO `childrenmenus` VALUES ('3', '出入信息', '103', 'gotomessage', '1');

-- ----------------------------
-- Table structure for dormitory
-- ----------------------------
DROP TABLE IF EXISTS `dormitory`;
CREATE TABLE `dormitory` (
  `nid` int NOT NULL AUTO_INCREMENT,
  `dormitory_id` int NOT NULL,
  `ceng_num` int NOT NULL,
  `bed_pid` int NOT NULL,
  `price` enum('1000','1500','2000') NOT NULL,
  `floor_id` varchar(5) NOT NULL,
  `isfull` enum('1','0') NOT NULL DEFAULT '0',
  `people` int DEFAULT NULL,
  PRIMARY KEY (`nid`),
  KEY `ix_dormitory_nid` (`nid`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of dormitory
-- ----------------------------
INSERT INTO `dormitory` VALUES ('1', '655', '6', '2', '1500', 'C1', '0', '0');
INSERT INTO `dormitory` VALUES ('2', '653', '6', '4', '2000', 'C1', '0', '0');
INSERT INTO `dormitory` VALUES ('3', '412', '5', '4', '1000', 'C2', '0', '0');
INSERT INTO `dormitory` VALUES ('4', '522', '5', '4', '2000', 'C2', '0', '0');
INSERT INTO `dormitory` VALUES ('5', '658', '6', '4', '2000', 'C4', '0', '0');
INSERT INTO `dormitory` VALUES ('6', '512', '5', '4', '1000', 'C5', '0', '0');
INSERT INTO `dormitory` VALUES ('7', '520', '5', '4', '2000', 'C5', '0', '0');
INSERT INTO `dormitory` VALUES ('8', '525', '5', '4', '2000', 'C5', '0', '0');
INSERT INTO `dormitory` VALUES ('9', '655', '5', '3', '2000', 'C2', '0', '0');
INSERT INTO `dormitory` VALUES ('10', '655', '5', '4', '1500', 'C3', '0', '0');
INSERT INTO `dormitory` VALUES ('11', '554', '5', '3', '2000', 'C3', '0', '0');
INSERT INTO `dormitory` VALUES ('12', '852', '5', '4', '2000', 'C3', '0', '0');

-- ----------------------------
-- Table structure for gotomessage
-- ----------------------------
DROP TABLE IF EXISTS `gotomessage`;
CREATE TABLE `gotomessage` (
  `goto_id` varchar(25) NOT NULL,
  `goto_name` varchar(10) NOT NULL,
  `goto_phone` varchar(22) NOT NULL,
  `goto_dormitory` varchar(10) NOT NULL,
  `goto_dormitory_id` varchar(10) NOT NULL,
  `goto_leavetime` varchar(25) DEFAULT NULL,
  `goto_backtime` varchar(25) DEFAULT NULL,
  `goto_reason` text,
  `goto_islate` enum('1','0') DEFAULT '0',
  PRIMARY KEY (`goto_id`),
  KEY `ix_gotomessage_goto_id` (`goto_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of gotomessage
-- ----------------------------
INSERT INTO `gotomessage` VALUES ('322', 'xzx', '13222222222', '222', 'C1', '2020-11-21T13:02:36.000Z', '2020-11-21T13:02:37.000Z', '哈哈哈哈', '0');
INSERT INTO `gotomessage` VALUES ('201810097123', '袁海', '13722222222', '525', 'C5', '2020-11-18T16:00:00.000Z', '2020-11-01T16:00:00.000Z', '泡妞', '0');
INSERT INTO `gotomessage` VALUES ('1322', '融入', '13222222222', '655', 'C3', '2020-11-24T16:25:31.000Z', '2020-11-24T16:25:33.000Z', '多么多么', '1');

-- ----------------------------
-- Table structure for house
-- ----------------------------
DROP TABLE IF EXISTS `house`;
CREATE TABLE `house` (
  `house_id` varchar(20) NOT NULL,
  PRIMARY KEY (`house_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of house
-- ----------------------------
INSERT INTO `house` VALUES ('C1');
INSERT INTO `house` VALUES ('C2');
INSERT INTO `house` VALUES ('C3');
INSERT INTO `house` VALUES ('C4');
INSERT INTO `house` VALUES ('C5');

-- ----------------------------
-- Table structure for menus
-- ----------------------------
DROP TABLE IF EXISTS `menus`;
CREATE TABLE `menus` (
  `ps_id` int NOT NULL AUTO_INCREMENT,
  `ps_pname` varchar(20) NOT NULL,
  `ps_pid` int DEFAULT NULL,
  `ps_level` enum('3','1','2') NOT NULL,
  PRIMARY KEY (`ps_id`)
) ENGINE=MyISAM AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of menus
-- ----------------------------
INSERT INTO `menus` VALUES ('101', '宿舍管理', null, '1');
INSERT INTO `menus` VALUES ('102', '学生管理', null, '1');
INSERT INTO `menus` VALUES ('103', '出入管理', null, '1');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `stu_id` varchar(25) NOT NULL,
  `stu_name` varchar(20) NOT NULL,
  `stu_gender` enum('男','女') NOT NULL,
  `stu_age` int NOT NULL,
  `stu_depart` varchar(20) NOT NULL,
  `stu_grade` varchar(5) NOT NULL,
  `stu_phone` varchar(22) NOT NULL,
  `stu_dormitory` int NOT NULL,
  `stu_dormitory_id` varchar(22) NOT NULL,
  PRIMARY KEY (`stu_id`),
  KEY `ix_student_stu_id` (`stu_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('1', 'dd', '男', '13', '计算机学院', '2019', '13222222222', '111', 'C1');
INSERT INTO `student` VALUES ('2', 'aa', '男', '13', '电气学院', '2019', '13222222222', '333', 'C1');
INSERT INTO `student` VALUES ('3', 'rr', '男', '13', '电气学院', '2019', '13222222222', '222', 'C1');

-- ----------------------------
-- Table structure for usertable
-- ----------------------------
DROP TABLE IF EXISTS `usertable`;
CREATE TABLE `usertable` (
  `username` varchar(8) NOT NULL,
  `password` varchar(16) NOT NULL,
  `radio` varchar(5) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of usertable
-- ----------------------------
INSERT INTO `usertable` VALUES ('admin', '123456', '1');
INSERT INTO `usertable` VALUES ('admin2', '123456', '2');
INSERT INTO `usertable` VALUES ('admin3', '123456', '3');
