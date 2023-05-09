/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.5.20-log : Database - yoga_poster_recognition
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`yoga_poster_recognition` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `yoga_poster_recognition`;

/*Table structure for table `doubt` */

DROP TABLE IF EXISTS `doubt`;

CREATE TABLE `doubt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `date` varchar(90) DEFAULT NULL,
  `doubts` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `trainer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `doubt` */

insert  into `doubt`(`id`,`user_id`,`date`,`doubts`,`reply`,`trainer_id`) values (1,27,'2/5/33','fffff','ok',3),(2,29,'2023-04-01','how are you','pending',30),(3,29,'2023-04-01','i am ok','pending',29),(4,32,'2023-04-08','how are you','pending',31),(5,31,'2023-04-08','i am ok','ok them',32),(6,31,'2023-05-04','say my name...','heisenberg',32),(7,31,'2023-05-06','i love me','so what',32);

/*Table structure for table `expert` */

DROP TABLE IF EXISTS `expert`;

CREATE TABLE `expert` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(90) DEFAULT NULL,
  `last_name` varchar(90) DEFAULT NULL,
  `phno` bigint(20) DEFAULT NULL,
  `place` varchar(90) DEFAULT NULL,
  `post` varchar(90) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `email_id` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `expert` */

insert  into `expert`(`id`,`login_id`,`first_name`,`last_name`,`phno`,`place`,`post`,`pin`,`email_id`) values (11,33,'Shahbas',' Al ameen',9874123547,'jdt vellimadu','kunnamangalam po',673574,'shahbas00@gmail.com'),(12,37,'vimal','vi ',9856457812,'farook','colege',673632,'vimalvi@gmail.com'),(13,40,'devika','mqq',8965471212,'kondotty','how',654578,'devika@gmail.com');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(200) DEFAULT NULL,
  `date` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`id`,`user_id`,`feedback`,`date`) values (1,4,'very good','2023-04-01'),(2,31,'good feed','2023-04-08'),(3,4,'','2023-04-09'),(4,31,'this is very helpful','2023-05-04'),(5,31,'very good web','2023-05-04'),(6,31,'ver gud app','2023-05-06');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(90) DEFAULT NULL,
  `password` varchar(90) DEFAULT NULL,
  `type` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values (1,'admin','123','admin'),(2,'ex','321','expert'),(3,'tr','456','trainer'),(4,'ur','789','user'),(6,'asd','asd','trainer'),(13,'sanjay','1234','user'),(27,'amal','v','user'),(29,'amal','amal','trainer'),(30,'amalbi','amalbi','user'),(31,'arjun','arjun','user'),(32,'nissam','nissam','trainer'),(33,'sha','sha','expert'),(34,'asf','asf','user'),(35,'anshad','anshad','user'),(36,'vimal','vi','trainer'),(37,'vi','vi','expert'),(38,'nirmal','nirmal','user'),(39,'kochu','kochu','rejected'),(40,'dev','dev','expert');

/*Table structure for table `time_register` */

DROP TABLE IF EXISTS `time_register`;

CREATE TABLE `time_register` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `date` varchar(90) DEFAULT NULL,
  `time` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `time_register` */

insert  into `time_register`(`id`,`user_id`,`date`,`time`) values (2,12,'2023/12/22','12:20-2:30'),(3,31,'2020/3.3/3','131');

/*Table structure for table `trainer_register` */

DROP TABLE IF EXISTS `trainer_register`;

CREATE TABLE `trainer_register` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `first_name` varchar(90) DEFAULT NULL,
  `last_name` varchar(90) DEFAULT NULL,
  `phno` bigint(20) DEFAULT NULL,
  `place` varchar(90) DEFAULT NULL,
  `post` varchar(90) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `mail_id` varchar(90) DEFAULT NULL,
  `experience` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `trainer_register` */

insert  into `trainer_register`(`id`,`log_id`,`first_name`,`last_name`,`phno`,`place`,`post`,`pin`,`mail_id`,`experience`) values (1,6,'SASSS','lkkk',0,'kkkjk','5678',6789,'cvbnm','cv'),(2,7,'asdfghjk','rtyuio',0,'fghjk','56789',6789,'fghjk','fghjkl'),(3,8,'asdfghjk','rtyuio',0,'fghjk','56789',6789,'fghjk','fghjkl'),(4,15,'amal','',0,'','',0,'',''),(5,16,'amal','a',1234569870,'calicut','calicut',123456,'amal@gmail.com','3'),(6,0,'','',0,'','',0,'',''),(7,29,'amal','vi',1234567899,'yigcgyh','kjgvh',62165,'iyciyv','jhgvh '),(8,32,'nissam','sahal',654654,'kina','seri',5465,'nissam@gmail.com','well experienced'),(9,36,'amal','vijay',9865457845,'farook','college',124578,'vi@gmail.com','2 years '),(10,39,'kochu','kutty',8954213256,'far','clg',656565,'kutty@gmail.com','12 years ');

/*Table structure for table `user_register` */

DROP TABLE IF EXISTS `user_register`;

CREATE TABLE `user_register` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(90) DEFAULT NULL,
  `last_name` varchar(90) DEFAULT NULL,
  `mail_id` varchar(90) DEFAULT NULL,
  `phno` bigint(20) DEFAULT NULL,
  `place` varchar(90) DEFAULT NULL,
  `post` varchar(90) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `user_register` */

insert  into `user_register`(`id`,`login_id`,`first_name`,`last_name`,`mail_id`,`phno`,`place`,`post`,`pin`) values (1,12,'mnbm',',jbjkb','kbjnb',0,'4654','65465456',0),(2,13,'sanjay','s ','vatakara',0,'674545','7894561230',0),(3,27,'amal','v','amalko@gmail.com',1234567890,'calicut','calicut',673632),(4,4,'ur','ur','ufiufhg',654654,'gu','35465',0),(5,30,'amal','bi','klhvbljh',6516,'6ugvgvohvh','6565',6465),(6,31,'arjun','v','arjun@gmail.com',9876543210,'ulli','molak',65465),(7,34,'aiswarya','kkk','as@gmail.com',9089788999,'ghjkl','fghj',789789),(8,35,'mhd','anshad','an@gmail.com',9845632127,'kon','tty',231245),(9,38,'nirmal','vi ','nirmal@gmail.com',8965478596,'azhi','nilam',695656);

/*Table structure for table `videos` */

DROP TABLE IF EXISTS `videos`;

CREATE TABLE `videos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `expert_id` int(11) DEFAULT NULL,
  `video` varchar(90) DEFAULT NULL,
  `date` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `videos` */

insert  into `videos`(`id`,`expert_id`,`video`,`date`) values (5,33,'pexels---16020561-2160x3840-25fps_1.mp4','2023-05-06');

/*Table structure for table `work` */

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `trainer_id` int(90) DEFAULT NULL,
  `status` varchar(90) DEFAULT NULL,
  `time` varchar(90) DEFAULT NULL,
  `date` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `work` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
