describe('Cypress Investown - find login 64', () => {
  it('find login link', () => {
    cy.visit('https://www.investown.cz')
    cy.contains('Přihlásit se').should('exist')
  })
})
