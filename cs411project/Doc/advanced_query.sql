-- Select all the products that are shown on both the wish list and the offer list
-- which has more than one provider.
SELECT w.Product_Name, o.Prodiving_Price, Provider_Name, Wisher_Name, o.Condition_status
FROM Wish_list w Join Offer_list o USING (Product_Name)
WHERE w.Product_Name in
    (SELECT o.Product_Name
    FROM Wish_list w Join Offer_list o USING (Product_Name)
    WHERE w.Product_Name = o.Product_Name 
    GROUP BY o.Product_Name
    HAVING COUNT(o.Product_Name) > 1)
ORDER BY w.Product_Name, o.Prodiving_Price;


-- Calculate the average price of each product provided by different platforms
(SELECT w.Product_Name, Provider_Name, avg(o.Prodiving_Price)
FROM Wish_list w JOIN Offer_list o ON w.Product_Name = o.Product_Name
GROUP BY Product_Name, Provider_Name)
UNION
(SELECT Product_Name, Merchant, avg(Highest_price)
FROM Transactions t
WHERE Merchant != ''   
GROUP BY Product_Name, Merchant);
