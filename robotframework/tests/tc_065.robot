*** Settings ***
Resource    ../resources/common.resource

*** Test Cases ***
RF-065 Check footer contains contact info
    Open Browser    ${DEMO_URL}    ${BROWSER}
    Page Should Contain    Kontakt
    Page Should Contain    info@
    Close Browser
