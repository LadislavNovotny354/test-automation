describe('Cypress Investown - find login 76', () => {
  it('find login link', () => {
    cy.visit('https://www.investown.cz')
    cy.contains('Přihlásit se').should('exist')
  })
})
