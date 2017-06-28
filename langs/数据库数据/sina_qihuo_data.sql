/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : sina_qihuo_data

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2016-02-08 23:18:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for futures_data
-- ----------------------------
DROP TABLE IF EXISTS `futures_data`;
CREATE TABLE `futures_data` (
`trade_category`  varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL ,
`trading_nit`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`price_quote`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`tick_size`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`limit_up_or_down`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`delivery_month`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`entry_timing`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`delivery_quality`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`delivery_point`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`transaction_code`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' ,
`Listexg`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`overhead_information`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
PRIMARY KEY (`transaction_code`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_bin

;

-- ----------------------------
-- Records of futures_data
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for 期货
-- ----------------------------
DROP TABLE IF EXISTS `期货`;
CREATE TABLE `期货` (
`交易品种`  varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL ,
`交易单位`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`报价单位`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`最小变动价位`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`涨跌停板幅度`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`合约交割月份`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`交易时间`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`交割品级`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`交割地点`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`交易代码`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' ,
`上市交易所`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`附加信息`  varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
PRIMARY KEY (`交易代码`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_bin

;

-- ----------------------------
-- Records of 期货
-- ----------------------------
BEGIN;
INSERT INTO `期货` VALUES ('美豆\r\n', '5000蒲式耳\r\n', '美分/蒲式耳\r\n', '0.25美分/蒲式耳\r\n', '70美分/蒲式耳，现货月合约无此限制\r\n', '1,3,5,7,8，9,11月\r\n', '北京时间（夏令时）22:30-03:00场内，06:00-03:00电子\r\n', 'CBOT规定的交割品级\r\n', 'S\r\n', 'S\r\n', '芝加哥商业集团\r\n', ''), ('豆粕\r\n', '10吨/手\r\n', '元(人民币/吨)\r\n', '1元/吨\r\n', '上一交易日结算价的±4%\r\n', '1,3,5,7,8,9,11,12月\r\n', '每周一到周五上午9:00-10:15,10:30-11:30，下午13:30-15:00\r\n', '合约月份第10个交易日\r\n', '大连商品交易所豆粕交割质量标准\r\n', '大连商品交易所豆粕交割质量标准\r\n', '合约价值的6%\r\n', '2元/手\r\n'), ('铁矿石\r\n', '100吨/手\r\n', '元（人民币）/吨 \r\n', '1元/吨\r\n', '上一交易日结算价的4％\r\n', '', '每周一至周五上午9:00～11:30，下午13:30～15:00\r\n', '合约月份第10个交易日\r\n', '大连商品交易所铁矿石交割质量标准\r\n', '大连商品交易所铁矿石交割质量标准\r\n', '合约价值的5%\r\n', ''), ('玻璃\r\n', '20吨/手\r\n', '元(人民币/吨)\r\n', '1元/吨\r\n', '上一交易日结算价的±4%\r\n', '1---12月\r\n', '每周一到周五上午9:00-10:15,10:30-11:30，下午13:30-15:00\r\n', '合约交割月份的第10个交易日\r\n', '合约交割月份的第12个交易日\r\n', '郑州商品交易所玻璃交割质量标准\r\n', '合约价值的6%\r\n', '3元/手，当日平仓手续费减半\r\n');
COMMIT;
