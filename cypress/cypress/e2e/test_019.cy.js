describe('Cypress Investown - offers 19', () => {
  it('navigates to offers', () => {
    cy.visit('https://www.investown.cz')
    cy.contains('Nabídka investic').click({force: true})
    cy.url().should('include', 'nabidka')
  })
})
