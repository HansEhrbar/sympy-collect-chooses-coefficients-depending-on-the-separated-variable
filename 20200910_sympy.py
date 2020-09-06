import sympy
sympy.init_printing(use_unicode=True)

alpha,beta,gamma,psi,theta,tau,CCC_2 = \
   sympy.symbols('alpha beta gamma psi theta tau CCC_2')

psi=theta*tau

CCC_2 = (alpha*psi+beta*theta+gamma*(psi+theta))**2 \
        -4*(alpha+beta+gamma)*gamma*psi*theta

sympy.pprint(sympy.collect(CCC_2, tau))



