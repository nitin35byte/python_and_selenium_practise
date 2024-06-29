*** Settings ***
Library     SeleniumLibrary
Library     Collections
Library     String


*** Variables ***
${URL}      https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
${input_email}      //input[@id='Email']
${input_password}       //input[@id='Password']
${click_login_btn}      //button[@type='submit']
${title}        //div[@class='title']
${expected_title}       Welcome, please sign in!
${E_T}      Your store. Login


${catalog}      //p[normalize-space()='Catalog']
${product_btn}      //p[text()=' Products']
${product_text}=        //h1[normalize-space()='Products']
${add_me}     //i[@class='fas fa-plus-square']
${Exp_product_txt}     Products
${add_product_title_xpath}     //title[normalize-space()='Add a new product / nopCommerce administration']
${add_product_title_exp}        Add a new product / nopCommerce administration
${product_name}     //input[@id='Name']
${short_desc}     //textarea[@id='ShortDescription']
${full_desc}        //body[@id='tinymce']
${sku}      //input[@id='Sku']
${drp_dwn}      //li[@class='select2-search select2-search--inline']/input[@class='select2-search__field' and @type='search']
${manu_drop}        (//li[@class='select2-search select2-search--inline']/input[@class='select2-search__field' and @type='search'])[2]
${user_added_succ-txt}=      //div[contains(@class,'success alert-dismissable')]                   
${exp_succ_msg}=     The new product has been added successfully.

${save_btn}=        //div[@class='content-header clearfix']//button[@name='save']
${manu_id}         //label[@for='SelectedManufacturerIds']
${chckbox}      //input[@id='Published']

*** Keywords ***
Login Functionality
    Open Browser        ${URL}      chrome
    ${extract_title}    Get Text    ${title}
    Should Be Equal As Strings    ${extract_title}    ${${expected_title}}
    Log To Console    ${extract_title}
    Maximize Browser Window
    Clear Element Text    ${input_email}
    Input Text    ${input_email}    admin@yourstore.com
    Clear Element Text    ${input_password}
    Input Text           ${input_password}      admin
    Click Element    ${click_login_btn}

Add Product
    [Documentation]     This method is created to add new product
    Click Element    ${catalog}
    Click Element    ${product_btn}
    ${product_valid}        Get Text    ${product_text}
    Log To Console    ${product_valid}
    Should Be Equal    ${product_valid}    ${Exp_product_txt}
    Click Element    ${add_me}
    Sleep    5s
    ${text_add_product}     Get Title
    Log To Console    ${text_add_product}
    Should Be Equal As Strings    ${text_add_product}    ${add_product_title_exp}
    Input Text    ${product_name}    nitin3
    Input Text    ${short_desc}     My nam is nitin i m writing automation script
    Select Frame        //iframe[@id='FullDescription_ifr']
    Click Element    ${full_desc}
    Input Text      ${full_desc}     My nam is nitin i m writing automation script
    Unselect Frame
    Input Text    ${sku}     Test AUtomation9
    Click Element   ${drp_dwn}
    Click Element    //li[text()='Computers']
    ##Select From List By Value      ${drp_dwn}      Computers
    Sleep    5s
    Click Element    ${manu_id}
    Sleep    2s
    Click Element   ${manu_drop}
    Sleep    2s
    Click Element    //li[text()='Apple']
    Checkbox Should Be Selected    ${chckbox}
    Sleep    3s
    Execute JavaScript    window.scrollTo(0, 0)
    Click Element    //div[@class='content-header clearfix']//button[@name='save']
    Sleep    10s
    ${success_message}      Get Text    ${user_added_succ-txt}
    Log To Console    ${success_message}
    Should Be Equal    ${success_message}    ${exp_succ_msg}
