*** Settings ***
Library     SeleniumLibrary
Library     Collections
Library     String
Resource    methods.robot



*** Test Cases ***
User Should be able to Login Successfully With Valid Cread
    [Tags]      Login_TC_01
    Login Functionality

Validate User Can add new product
    [Tags]      Login_TC_02
    [Documentation]     user shoule be able to add new product
    Login Functionality
    Add Product