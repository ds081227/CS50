-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Retrieve the crime report on July 28 that took place on Humphrey Street
SELECT * FROM crime_scene_reports
WHERE street = 'Humphrey Street'
AND month = 7
AND day = 28;
-- The crime_scene_report ID 295 is the CS50 duck theft, took place in 2023/7/28 10:15am at the Humphrey Street Bakery, three witnesses present.

-- Retrieve the interview transcript of the crime
SELECT * FROM interviews
WHERE year = 2023 AND month = 7 AND day = 28;
-- interviews id 161 : the thief get into a car within ten minutes of theft and drive away
-- interview id 162: Earlier in the morning before she arrived at bakery, saw the thief retrieving money in Leggett Street ATM
-- interivew id 163: called someone and talked to them for less than a minute, take the earliest flight out of fiftyville tomorrow

-- Retrieve the security logs from bakery store, check cars that exit after the crime scene time(10 minutes time frame)
SELECT * FROM bakery_security_logs
WHERE year = 2023 AND month = 7 AND day = 28
AND hour = 10 AND 15 <= minute AND minute <= 25;
-- Found 8 cars exiting within the 10minute frame

-- Retrieve the ATM transaction on that day before the crime scene's time
SELECT * FROM atm_transactions
WHERE year = 2023 AND month = 7 AND day = 28
AND atm_location = 'Leggett Street';

-- Check the phone call record after crime scene time
SELECT * FROM phone_calls
WHERE year = 2023 AND month = 7 AND day = 28
AND duration <= 60;

-- Join the people table on car plate, phone number, bank transaction to narrow down the data size
SELECT * FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions on atm_transactions.account_number = bank_accounts.account_number
WHERE phone_calls.year = 2023 AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration <= 60
AND bakery_security_logs.hour = 10 AND 15 <= bakery_security_logs.minute AND bakery_security_logs.minute <= 25
AND atm_location = 'Leggett Street'
AND people.name = 'Diana';
-- Narrowed down to two person, Bruce and Diana

-- Find the airport name for fiftyville
SELECT * FROM airports
WHERE city like '%fiftyville%'
-- id 8, Fiftyville Regional Airport

-- Find earliest flight that leaves fiftyville
SELECT * FROM flights
WHERE year = 2023 AND month = 7 AND day = 29
AND origin_airport_id = 8
ORDER BY hour;
-- flight id is 36, destination airport id 4, 8:20am start flight

-- Crosscheck the old data with the flight number
SELECT * FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions on atm_transactions.account_number = bank_accounts.account_number
JOIN passengers ON passengers.passport_number = people.passport_number
WHERE phone_calls.year = 2023 AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration <= 60
AND bakery_security_logs.hour = 10 AND 15 <= bakery_security_logs.minute AND bakery_security_logs.minute <= 25
AND atm_location = 'Leggett Street'
AND passengers.flight_id = 36;
-- Found only 1 match, Bruce

-- Get the destination airport
SELECT * FROM airports
WHERE id = (
    SELECT destination_airport_id FROM flights
    WHERE id = 36
);
-- LaGuardia Airport, New York City

--Find out who did Bruce call
SELECT * FROM people
WHERE phone_number = (
    SELECT receiver FROM phone_calls
    JOIN people ON people.phone_number = phone_calls.caller
    WHERE phone_calls.year = 2023 AND phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration <= 60
    AND people.name = 'Bruce'
);
-- Answer is Robin
