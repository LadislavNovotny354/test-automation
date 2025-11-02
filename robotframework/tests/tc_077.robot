*** Settings ***
Resource    ../resources/common.resource

*** Test Cases ***
RF-077 Check cookie banner presence and accept
    Open Browser    ${DEMO_URL}    ${BROWSER}
    Run Keyword And Ignore Error    Click Button    Přijmout
    Close Browser
