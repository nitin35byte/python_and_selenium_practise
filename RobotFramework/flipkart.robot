*** Setting ***
Library     SeleniumLibrary
Library     Collections
Library     String


*** Variable ***
${url}=     https://www.flipkart.com/
${serach_box}=      //input[@class='Pke_EE']
${listed_product}=      //div[@class='col col-7-12']
${validation}=      //div[@class='E2lCdq']
${check_pincode}=       //input[@class='AFOXgu']
${check}=       //span[text()='Check']
${add-to_cart}=     //button[@class='QqFHMw vslbG+ In9uk2']
${price1item}=      //div[@class='HRZecL']//div[@class='k9WPjB'])[1]
${price1item_price}=        //div[@class='HRZecL']//div[@class='k9WPjB'])[1]//..//..//span
${Discount}=      (//div[@class='k9WPjB'])[2]
${Discount_price}=        (//div[@class='k9WPjB'])[2]//..//..//span
${deliverycharges}=      (//div[@class='k9WPjB'])[2]
${deliverychargesprice}=        (//div[@class='k9WPjB'])[3]//..//..//span
${total_amount}=        //div[@class='V2UaYI']
${amount}=      (//div[@class='_1Y9Lgu'])[1]

*** Keyword ***
Search Product
    Open Browser    ${url}      Chrome
    Maximize Browser Window
    Input Text      ${serach_box}       iphone15
    Press Keys      ${None}     BACKSPACE
    Sleep    2s
    Input Text      ${serach_box}       iphone15
    Press Keys      ${None}     ENTER
#    Press Key       ${search_box}       ENTER

Extract Product
    Click Element   ${listed_product}
    Switch Window       New
    Sleep    5s
   #3Page Should Contain    ${validation}
    ${deal_text}        Get Text    ${validation}
    Log To Console    dela of the day is :${deal_text}

#    FOR    ${ITEMS}    IN    @{listed_products}
#        Log    ${ITEMS}
#    END
Add To Card
    Input Text    ${check_pincode}    110059
    Click Element    ${check}
    Sleep    3s
    Click Element    ${add-to_cart}
    Page Should Contain    Price details
    ${test_1}=      Get Text    ${price1item}
    Log To Console    ${test_1}

    Should Be Equal As Strings    ${test_1}    Price (1 item)
    ${price1item_price_1}=      Get Text    ${price1item_price}
    Log To Console    ${price1item_price_1}

    ${test_2}=      Get Text    ${price1item}
    Log To Console    ${test_2}
    Should Be Equal As Strings    ${test_1}    Discount
    ${Discount_1}=      Get Text    ${Discount_price}
    Log To Console    ${Discount_1}

    ${test_3}=      Get Text    ${deliverycharges}
    Log To Console    ${test_3}
    Should Be Equal As Strings    ${test_3}   Delivery Charges
    ${Discount_2}=      Get Text    ${deliverychargesprice}
    Log To Console    ${Discount_2}

    ${test_4}=      Get Text    ${total_amount}
    Log To Console    ${test_4}
    Should Be Equal As Strings    ${test_4}   Total Amount

    ${ampunt_1}=      Get Text    ${amount}
    Log To Console    ${ampunt_1}

    ${test_5}=   Get Text   (//div[@class='IbVNxe'])[1]
    Log To Console    ${test_5}

*** Test Case ***
Serch product on flipkart
    [Documentation]
    [Tags]      TC_01       Flipkart
    Search Product


Extarct Product details
    [Tags]      TC_02       Flipkart
    Search Product
    Extract Product


Add to Cart Product
    Search Product
    Extract Product
    Add To Card












