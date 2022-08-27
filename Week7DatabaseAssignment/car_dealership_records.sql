-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 27, 2022 at 09:41 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car_dealership_records`
--

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_info`
--

CREATE TABLE `vehicle_info` (
  `record_number` int(10) NOT NULL,
  `vehicle_make` varchar(50) NOT NULL,
  `vehicle_model` varchar(50) NOT NULL,
  `VIN_number` varchar(20) NOT NULL,
  `owner_name` varchar(100) DEFAULT NULL,
  `price_paid` float DEFAULT NULL,
  `sales_price` float NOT NULL,
  `vehicle_description` varchar(300) NOT NULL,
  `Deleted` varchar(10) NOT NULL DEFAULT 'NO'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_info`
--

INSERT INTO `vehicle_info` (`record_number`, `vehicle_make`, `vehicle_model`, `VIN_number`, `owner_name`, `price_paid`, `sales_price`, `vehicle_description`, `Deleted`) VALUES
(1, 'Toyota', 'Avalon', '123456', 'Joe Hartwick', 4000, 3000, 'A small 5 seater vehicle with very high energy efficently.', 'YES'),
(2, 'Chrysler', 'Pacifcia', '123456678', 'Lindemuth, Sharon', 2300.67, 3546.87, 'A 7-seater vehicle with built-in navigation features', 'YES'),
(3, 'Toyota', 'Tundra', '132458334', 'Hartwick, Julie', 1678.25, 2000.86, 'A five-seater pickup truck with extra legroom and heated and cooling seats. ', 'NO'),
(4, 'Ford', 'F150', '123765', 'Petz, Tom', 3000, 4000, 'A pickup truck with 5 seats and a sunroof', 'NO'),
(5, 'Chrysler', '300', '1234567', NULL, NULL, 4000.67, 'A five seater vehicle with all wheel drive', 'NO'),
(6, 'Ford', '500', '123456786', NULL, NULL, 4000.67, 'A five seater vehicle with all wheel drive', 'YES');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `vehicle_info`
--
ALTER TABLE `vehicle_info`
  ADD PRIMARY KEY (`record_number`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `vehicle_info`
--
ALTER TABLE `vehicle_info`
  MODIFY `record_number` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
