*** settings ***
Library     SeleniumLibrary
Library     Collection
*** variables ***
${url}      https://www.flipkart.com/
${login_btn}        //span[text()='Login']
${txt}=     //input[@class='r4vIwl BV+Dqf']
${locator}=     //*[@class='KIOyzU']
${actual_txt}=      Please enter valid Email ID/Mobile number
${txt_1}=       Login

*** keywords ***
please hhhhhhhh
    Open Browser    ${url}      Chrome
    Run Keyword And Ignore Error    Scroll Element Into View    //*[@aria-label='Myntra']
    Click Element    //*[@aria-label='Myntra']
    Click Element   ${login_btn}
    Input Text      ${txt}      9999999
    Page Should Contain     Login
    Page Should Contain    Please enter valid Email ID/Mobile number
    Run Keyword And Ignore Error    Scroll Element Into View    //*[@aria-label='Myntra']
    Click Element    //*[@aria-label='Myntra']
    ${txt}=      Get Text    ${locator}
    Should Be Equal    ${txt}    ${txt_1}
    Log To Console        ${txt_1}

    ##Should Be Equal    ${txt}    ${txt_1}
    

*** test cases ***
tesr data
    please hhhhhhhh