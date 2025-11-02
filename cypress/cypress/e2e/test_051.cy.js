describe('Cypress Investown - title check 51', () => {
  it('title contains Investown', () => {
    cy.visit('https://www.investown.cz')
    cy.title().should('include', 'Investown')
  })
})
