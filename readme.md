# Weather app 1.0
## Summary
The program in which you enter the name of the city you are interested in to get up-to-date information about the local weather.
Information is obtained through the use of a third party [API](https://openweathermap.org/api).

## Pre-conditions
Before using the program, you will need to obtain your personal **API key** and install all the necessary dependencies located in the file `req.txt`

## Usage
1. Getting API key.
   1. Register: [openweather.org](https://openweathermap.org/);
   2. Sign in;
   3. Click on your account name in the upper right corner of the screen and go to the tab **"My API keys"**;
   4. Copy the key and paste into a text file ***"api-key"***, located in the folder **"content"**.
2. Launch the program and enter the name of the city you are interested in. Input can work with both Cyrillic and Latin alphabet.
```terminal
Please, enter the city: Sarov
```
3. We get the output in the following format:
```Terminal
        City: Sarov
        --------------------------------------
        temperature: -5℃
        feels_like: -8℃
        humidity: 97%
        weather: overcast clouds
        --------------------------------------
```