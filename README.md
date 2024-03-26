# Bot for bidding on Yahoo auctions JP on FromJapan

FromJapan is a shopping and auction proxy purchasing service that allows for overseas users to make bids on auctions in Japan (The most popular being Yahoo! Japan Auction)
This project runs a script written with Python and utilizes Selenium to mimic a user's actions. The idea is to place bids automatically on a listing that will soon be ending. It will perform the following:
1. Enter the user's provided email and password in the script to log into the FromJapan account
2. Navigate to the listing's page through a provided URL
3. Find the current bid number and the time left renaming on the auction. It will only run when there's less than 5 minutes less on the auction
4. Enter a bid price that will be 20 yen higher than the current bid, click on the 'Place Real-Time Bid' button and also click on the 'Confirm' button
5. Cross reference if the current updated bid price is what was entered on our end. If not, then someone else has bidded so increase the bid again by 20 yen. Otherwise refresh the page

1. ![FromJapanStep1](https://github.com/CamyKam/Python_Auction_Bot/assets/60831407/ee9ad1ea-6fa8-4a07-b8d9-847f5b032d15)
2. ![FromJapanStep2](https://github.com/CamyKam/Python_Auction_Bot/assets/60831407/b0843288-15fc-40a4-ac8f-7f8d8b253c3a)
3. ![FromJapanStep3](https://github.com/CamyKam/Python_Auction_Bot/assets/60831407/62f224c8-97ce-4939-88d2-55c2dbe9e69d)
4. ![FromJapanStep4](https://github.com/CamyKam/Python_Auction_Bot/assets/60831407/9d702283-648f-44e9-bdbe-29026521e713)

The script will then return to the listing page again and will wait or bid
