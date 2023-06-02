# BudgetScan

BudgetScan is a basic budgeting app whose main goal is to be able to deduct the price on a receipt from an account by simply scanning it. My initial intention with this project was to link it directly to my banks API but then I found that my bank does not directly have an API and I was skeptical in choosing third-party service.

You might ask that simply entering the total on a receipt is easier than clicking a picture, which is true, but My goal with this is to possibly classify all the Items in the receipt in categories like grocery, produce etc. (and also because it looks cool).

## Table of Contents
- [Overview](#overview)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
   - [The Receipt Scanner](#the-receipt-scanner)
  - [login](#loginregister)
  - [Account System](#account-system)
  - [What I learned](#what-i-learned)
- [Author](#author)

## Overview


### Screenshot

![/screenshot.png](./screenshot.png)


The project has multiple components:

## My process

### Built with

- Flask
- OCRspace API
- SQLAlchemy 

### The Receipt Scanner

The receipt scanner uses a free API called OCRspace. The image is passed to the function which makes the API call and then returns the parsed text.

The API is highly configurable, it can specifically be set to scan for receipt/table content using the `isTable` property.

The API has multiple engines, and I found the engine 2 to be the best in terms of accuracy.

Currently, the Scanner only looks for the word 'TOTAL' in the image and then finds the total in the receipt.

But as mentioned, I will be working upon a version which actually classifies the purchased items into categories for budget management.

### login/register

The login uses sqlAlchemy databases to actually create an account.

Basic SQL database.

### Account System

Each user can create and delete multiple banking accounts. They can start with a particular balance and then set an account as their default.

The default account is used to deduct the receipt total if another account is not specifically specified.

Balance transfer is also a feature.

