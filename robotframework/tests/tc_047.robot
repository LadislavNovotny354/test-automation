*** Settings ***
Resource    ../resources/common.resource

*** Test Cases ***
RF-047 Check cookie banner presence and accept
    Open Browser    ${DEMO_URL}    ${BROWSER}
    Run Keyword And Ignore Error    Click Button    Přijmout
    Close Browser
