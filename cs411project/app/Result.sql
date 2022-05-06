DELIMITER //
CREATE PROCEDURE Result(IN product VARCHAR (255), IN price REAL)
    BEGIN
        DECLARE custInfo CURSOR For
            (SELECT * FROM(
            (SELECT Product_Name, Provider_Name, avg(Prodiving_Price)
            FROM Offer_list o
            GROUP BY Product_Name, Provider_Name)
            UNION
            (SELECT Product_Name, Merchant, avg(Highest_price)
            FROM Transactions t
            WHERE Merchant != ''   
            GROUP BY Product_Name, Merchant)) as t3
            WHERE Product_Name = product);

        DECLARE custInfo2 CURSOR For
            (SELECT w.Product_Name, o.Prodiving_Price, Provider_Name
            FROM Wish_list w Join Offer_list o USING (Product_Name)
            WHERE w.Product_Name in
                (SELECT o.Product_Name
                FROM Wish_list w Join Offer_list o USING (Product_Name)
                WHERE w.Product_Name = o.Product_Name 
                GROUP BY o.Product_Name
                HAVING COUNT(o.Product_Name) > 1)
            ORDER BY w.Product_Name, o.Prodiving_Price);

        DROP TABLE IF EXISTS HotProducts;
        CREATE TABLE HotProducts(
                    Product_Name VARCHAR(255),
                    Prodiving_Price REAL,
                    Provider_Name VARCHAR(255),
                    PRIMARY KEY (Product_Name, Provider_Name)); 

        DROP TABLE IF EXISTS MerchantTable;
        CREATE TABLE MerchantTable(
                    Product_Name VARCHAR(255),
                    Merchant_Name VARCHAR(50),
                    Providing_Price REAL,
                    PRIMARY KEY (Merchant_Name));  
           
        OPEN custInfo;
        BEGIN
            DECLARE varproduct_name VARCHAR(255);
            DECLARE varmerchant_name VARCHAR(50);
            DECLARE varproviding_price REAL;
            DECLARE loop_exit BOOLEAN DEFAULT FALSE;
            DECLARE CONTINUE HANDLER FOR NOT FOUND SET loop_exit = TRUE;

            cloop: LOOP
                FETCH custInfo INTO varproduct_name, varmerchant_name, varproviding_price;
                IF loop_exit THEN
                    LEAVE cloop;
                END IF;
            
                IF (varproviding_price < price) THEN
                    INSERT IGNORE INTO MerchantTable(Product_Name, Merchant_Name, Providing_Price)
                    VALUES (varproduct_name, varmerchant_name, varproviding_price);
                END IF;
            END LOOP cloop;
        END;
        CLOSE custInfo;

        OPEN custInfo2;
        BEGIN
            DECLARE varproductname VARCHAR(255);
            DECLARE varprodivingprice REAL;
            DECLARE varprovidername VARCHAR(255);
            DECLARE loop_exit BOOLEAN DEFAULT FALSE;   
            DECLARE CONTINUE HANDLER FOR NOT FOUND SET loop_exit = TRUE;

            cloop: LOOP
                FETCH custInfo2 INTO varproductname, varprodivingprice, varprovidername;
                IF loop_exit THEN
                    LEAVE cloop;
                END IF;

                INSERT IGNORE INTO HotProducts(Product_Name, Prodiving_Price, Provider_Name)
                VALUES (varproductname, varprodivingprice, varprovidername);
            END LOOP cloop;
        END;
        CLOSE custInfo2;

    END;//


-- Sonic Alert Sb300ss Sonic Boom Alarm Clock White

-- #test
-- SELECT * FROM(  (SELECT Product_Name, Provider_Name, avg(Prodiving_Price)             FROM Offer_list o             GROUP BY Product_Name, Provider_Name)             UNION
--          (SELECT Product_Name, Merchant, avg(Highest_price)             FROM Transactions t             WHERE Merchant != ''                GROUP BY Product_Name, Merchant)) as t3             
--          WHERE Product_Name = "Sonic Alert Sb300ss Sonic Boom Alarm Clock White";

-- INSERT INTO MerchantTable(Product_Name, Merchant_Name, Providing_Price)
-- VALUES ("product_name", "merchant_name", 1);

INSERT IGNORE INTO HotProducts(Product_Name, Prodiving_Price, Provider_Name)
VALUES ("varproductname", "varprodivingprice", "varprovidername");


DELIMITER //
CREATE PROCEDURE Result(IN product VARCHAR (255), IN price REAL)
    BEGIN
        DECLARE varproduct_name VARCHAR(255);
        DECLARE varmerchant_name VARCHAR(50);
        DECLARE varproviding_price REAL;
        DECLARE loop_exit BOOLEAN DEFAULT FALSE;
               
        DECLARE custInfo CURSOR For
            (SELECT * FROM(
            (SELECT Product_Name, Provider_Name, avg(Prodiving_Price)
            FROM Offer_list o
            GROUP BY Product_Name, Provider_Name)
            UNION
            (SELECT Product_Name, Merchant, avg(Highest_price)
            FROM Transactions t
            WHERE Merchant != ''   
            GROUP BY Product_Name, Merchant)) as t3
            WHERE Product_Name = product);

        DECLARE CONTINUE HANDLER FOR NOT FOUND SET loop_exit = TRUE;
       
        DROP TABLE IF EXISTS MerchantTable;
        CREATE TABLE MerchantTable(
                    Product_Name VARCHAR(255),
                    Merchant_Name VARCHAR(50),
                    Providing_Price REAL,
                    PRIMARY KEY (Merchant_Name));  
           
        OPEN custInfo;
        cloop: LOOP
            FETCH custInfo INTO varproduct_name, varmerchant_name, varproviding_price;
            IF loop_exit THEN
                LEAVE cloop;
            END IF;
           
            IF (varproviding_price < price) THEN
                INSERT IGNORE INTO MerchantTable(Product_Name, Merchant_Name, Providing_Price)
                VALUES (varproduct_name, varmerchant_name, varproviding_price);
            END IF;
        END LOOP cloop;
        CLOSE custInfo;
    END;//