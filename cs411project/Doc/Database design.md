## Command to connect sql
mysql -h 34.136.51.71 -u yuhao

## How we create table (You may refer to the setup.sql)
 <pre> 
CREATE TABLE Product (  
    Brand VARCHAR(255), 
    Manufactor VARCHAR(255),
    Manufactor_Number VARCHAR(255), 
    Product_Name VARCHAR(255), 
    Category VARCHAR(255), 
    Product_Weight VARCHAR(255), 
    PRIMARY KEY (Product_Name) 
);  
</pre>
<pre> 
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
</pre> 
<pre> 
CREATE TABLE Wish_list (  
    Wish_ID INT UNSIGNED AUTO_INCREMENT,  
    Create_Date VARCHAR(50),  
    Acceptable_Price Real,  
    Wisher_Name VARCHAR(50),  
    Product_Name VARCHAR(255),  
    PRIMARY KEY (Wish_ID)  
    -- FOREIGN KEY (Wisher_Name) REFERENCES User(Users_Name) on delete CASCADE on update CASCADE  
);
</pre> 
<pre> 
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
</pre> 
<pre> 
CREATE TABLE User (  
    Users_ID INT UNSIGNED AUTO_INCREMENT,  
    Users_Password VARCHAR(50),  
    Users_Name VARCHAR(50),  
    Birthday VARCHAR(50),  
    PRIMARY KEY (Users_ID)  
);
</pre> 

## Advanced SQL queries (You may refer to the advanced_query.md)

-- Select all the products that are shown on both the wish list and the offer list  
-- which has more than one provider.
<pre> 
SELECT w.Product_Name, o.Prodiving_Price, Provider_Name, Wisher_Name, o.Condition_status  
FROM Wish_list w Join Offer_list o USING (Product_Name)  
WHERE w.Product_Name in  
    (SELECT o.Product_Name  
    FROM Wish_list w Join Offer_list o USING (Product_Name)  
    WHERE w.Product_Name = o.Product_Name   
    GROUP BY o.Product_Name  
    HAVING COUNT(o.Product_Name) > 1)  
ORDER BY w.Product_Name, o.Prodiving_Price 
LIMIT 15;  

</pre> 
-- Calculate the average price of each product provided by different platforms and provides the average price from our user sellers
<pre> 
(SELECT o.Product_Name, o.Provider_Name, avg(o.Prodiving_Price)  
FROM Wish_list w JOIN Offer_list o ON w.Product_Name = o.Product_Name  
GROUP BY Product_Name, Provider_Name)  
UNION  
(SELECT Product_Name, Merchant, avg(Highest_price)  
FROM Transactions t  
WHERE Merchant != ''     
GROUP BY Product_Name, Merchant)  
ORDER BY Product_Name 
LIMIT 15;  
</pre> 

## Analysis about the index

### Three index methods tried
0. No index
1. Index the Merchant and Product_Name          of the Transactions table 

2. Index the Product_Name                       of the Offer_list table
   Index the Product_Name                       of the Wish_list table
   Index the Product_Name                       of the Transactions table
  
3. Index the Product_Name and the Provider_Name of the Offer_list table
   Index the Product_Name                       of the Wish_list table
   Index the Merchant and Product_Name          of the Transactions table 




### Result and Analysis
0: Query1: 0.19s

   Query2: 0.30s
   
1: Query1: 0.24s

   Query2: 0.09s
   
The Query 1 is not better. We think it is because the query itself has nothing to do with the Transactions table while we just put index on that table.

The Query 2 is faster. We think it is because the Merchant and Product_Name is indexed, so it will be faster when we group by Product_Name, Merchant and calculate the average.
   
2: Query1: 0.01s

   Query2: 0.05s
   
The Query 1 is much faster. We think that because when we add index of the Product_Name to all the three tables, it will make the "join" process much faster as well as the "group by". 

The Query 2 is also much faster. The reason is similiar to the first one. Adding index of the Product_Name to all the three tables may save a lot of time when we join tables.
   
Addition comment: The result is much faster than we thought. But we tried many times on this index implementation resulting in the same outcomes.
   
3: Query1: 0.01s

   Query2: 0.07s
   
   
The query 1 is as fast as the index implementation in index combination 2 above. We find it as expected as the change of index from Product_Name to (Provider_Name, Product_Name) does not change the Offer_list table much as there are not several repeating Product_Names in the Offer_list. As a result, the extra indexing of Provider_Name does not mean much for runtime.

The query 2 is faster than index implmentation in index combination 1 above as the query has union between one query that uses Offer_list and Wish_list and another that only uses Transactions table. By additionally indexing Offer_list by (Provider_Name, Product_Name) and Wish_list by Product_Name, it makes one query of the union faster, hence faster than index combination in 1. 

The query 2 is slower than index implementation in index combination 2 above as we see from index combination 1 and 2 that indexing Transactions by (Merchant, Product_Name) is more inefficent than indexing Transactions by Product_Name alone. In this index implemenation (index implemenatation 3), we have Transactions indexed by (Merchants, Product_Name) which is slower than indexing Transactions by just Product_Name, hence the query 2 runtime for index implmentation 3 is between runtime of index implemnation 1 and 2.

Addition comment: The result is much faster than we thought. But we tried many times on this index implementation resulting in the same outcomes.

   



