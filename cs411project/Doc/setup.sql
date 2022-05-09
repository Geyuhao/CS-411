CREATE TABLE Product (
    Brand VARCHAR(255),
    Manufactor VARCHAR(255),
    Manufactor_Number VARCHAR(255),
    Product_Name VARCHAR(255),
    Category VARCHAR(255),
    Product_Weight VARCHAR(255),
    PRIMARY KEY (Product_Name)
);

CREATE TABLE Transactions (
    Transaction_ID INT UNSIGNED AUTO_INCREMENT,
    Highest_price Real,
    Lowest_price Real,
    Availible_status VARCHAR(255),
    Condition_status VARCHAR(255),
    Merchant VARCHAR(255),
    Product_Name VARCHAR(255),
    PRIMARY KEY (Transaction_ID),
    FOREIGN KEY (Product_Name) REFERENCES Product(Product_Name) on delete CASCADE on update CASCADE
);

CREATE TABLE Wish_list (
    Wish_ID INT UNSIGNED AUTO_INCREMENT,
    Create_Date VARCHAR(50),
    Acceptable_Price Real,
    Wisher_Name VARCHAR(50),
    Product_Name VARCHAR(255),
    PRIMARY KEY (Wish_ID)
    -- FOREIGN KEY (Wisher_Name) REFERENCES User(Users_Name) on delete CASCADE on update CASCADE
);

CREATE TABLE Offer_list (
    Offer_ID INT UNSIGNED AUTO_INCREMENT,
    Create_Date VARCHAR(50),
    Prodiving_Price Real,
    Provider_Name VARCHAR(50),
    Product_Name VARCHAR(255),
    Condition_status VARCHAR(50),
    PRIMARY KEY (Offer_ID)
    -- FOREIGN KEY (Provider_Name) REFERENCES User(Users_Name) on delete CASCADE on update CASCADE
);

CREATE TABLE User (
    Users_ID INT UNSIGNED AUTO_INCREMENT,
    Users_Password VARCHAR(50),
    Users_Name VARCHAR(50),
    Birthday VARCHAR(50),
    PRIMARY KEY (Users_ID)
);




