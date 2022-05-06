DELIMITER //

CREATE TRIGGER newproduct
    AFTER INSERT ON Offer_list
    FOR EACH ROW
    BEGIN
        IF New.Product_Name NOT IN (SELECT Product_Name FROM Product) THEN
            INSERT INTO Product(Product_Name)
            VALUES(New.Product_Name);
        END IF;
    END;//

DELIMITER;