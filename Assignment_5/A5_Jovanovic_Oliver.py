# 1. Research:
# Question:
# Choose and gather information about an infection or a Virus.
# Answer:
# I choose Norovirus.
# Question:
# Gather Information about a population where an outbreak has occurred or could happen:
# Answer:
# Norovirus has 685 million cases and 200,000 deaths per year. Anyone can get infected.
# Question:
# Choose a time frame (in days) for the model and/or the forecast
# Answer:
# Incubation time is 12 - 48 hours, it lasts for up to three days.
# The model will have a time period of 5 days.
# see: https://en.wikipedia.org/wiki/Norovirus .
# Question:
# Depending on the selected infectious disease, what compartments are there in the population?
# Answer:
# see: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5851036/ .
# Question:
# Define the factors that influence an outbreak either by using credible sources or by providing them by
# yourself with justification.
# Answer:
# see: https://www.cdc.gov/norovirus/index.html
# Spreads from infected people to others or through contaminated foods and surfaces. They occur most often Nov. - Apr.
# Question:
# Primarily: Susceptibility, infection rate, immunity
# Answer:
# Susceptibility: Everyone can get, unless there is a presence or absence of HBGAs (depends on Virus genome).
# Infection rate: (685,000,000 / 8,000,000,000) * 100 = 8.5625%.
# Immunity: People with the presence or absence of human histoblood group antigens (HBGAs) are not very susceptible for
# Norovirus, e.g. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6466115/#:~:text=Despite%20their%20high%20infectivity%2C%20a,HBGAs)%20on%20gut%20epithelial%20surfaces.
# Question:
# Define the interventions that could have been / were undertaken to control the outbreak.
# Answer:
# A lot of preventive measures can be made, e.g. compliance with hygiene rules, cleaning surfaces directly after using etc.
# Measures while being infected with Norovirus are:
# Isolation, compliance with hygiene rules, a lot of drinking, ventilate rooms, personal laundry etc.
# see: https://www.rki.de/DE/Content/Infekt/EpidBull/Merkblaetter/Ratgeber_Noroviren.html;jsessionid=B83068F8B0AF74955B92F6999E764A77.internet051#doc2374562bodyText12
# Question:
# How did you define the intervention factors in the equations? What are the values based on?
# Answer:
# ---
# Question:
# Determine which variables are available and can be used to model this event
# Answer:
# see: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5851036/
# Question:
# What is R0? How is it different to Re? Note the answer down.
# Answer:
# R0 is a biological constant for a specific pathogen and is the derivative from the "duration of infectivity after the
# patient gets infected", "the likelihood of transmission of infection per contact between a susceptible person and an
# infectious individual" and "the contact rate". So it is an estimate of the contagiousness for the human behaviour.
# Re on the other side is the effective reproduction number and describes the number of people in a population that
# can be infected at any specific time. The factors that affect Re are "the number of people with infection",
# "the number of susceptible people with whom infected people are in contact", "and people's behaviour", e.g social distancing.
# see: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7751056/

# 2. Based on the data, create 2 scenarios and model:
# - an outbreak in a population
#   - plot a graph showing the values for each compartment over time.

# Customized code based on Mariia Gontas code:
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N.
N = 1000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Exposure:
# e.g. https://www.sciencedirect.com/science/article/pii/S1755436513000546
E0 = 1
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.2, 1. / 10
# transmission rate, alpha and per-capita birth or death rate, mu.
# e.g. https://pubmed.ncbi.nlm.nih.gov/32087775/#:~:text=The%20microbiologically%20confirmed%20symptomatic%20transmission,21%20of%20119%20household%20members).
# e.g. https://bmcinfectdis.biomedcentral.com/articles/10.1186/s12879-019-4007-2#:~:text=A%20systematic%20review%20of%2039,per%20100%2C000%20persons%20%5B21%5D.
alpha, mu = 0.1, 3.2 / 100000
# A grid of time points (in days)
t = np.linspace(0, 80, 80)

# The SEIR model differential equations.
def deriv(y, t, N, alpha, beta, gamma, mu):
    S, E, I, R, = y
    dSdt = mu * N - beta * S * I - mu * S
    dEdt = beta * S * I - alpha * E - mu * E
    dIdt = alpha * E - gamma * I - mu * I
    dRdt = gamma * I - mu * R
    return dSdt, dEdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, E0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, alpha, beta, gamma, mu))
S, E, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S / 1000, 'b', alpha=.5, lw=2, label='Susceptible')
ax.plot(t, E / 1000, 'k', alpha=.5, lw=2, label='Exposure')
ax.plot(t, I / 1000, 'r', alpha=.5, lw=2, label='Infected')
ax.plot(t, R / 1000, 'g', alpha=.5, lw=2, label='Recovered with immunity')
ax.set_title('SEIR Model: Norovirus')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0, 1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(visible=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()
del E, E0, I, I0, N, R, R0, S, S0, alpha, ax, beta, fig, gamma, legend, mu, ret, spine, t, y0

# - an outbreak with introduction of an intervention in a population
#   - plot a graph showing the values for each compartment over time
#   - you can introduce 1 or more interventions
#   - how did you choose the rates for the interventions?
# The only intervention is that the people look after their hygiene. I assume that there are probably 10% of people who
# do this on regular basis.
# Total population, N.
N = 1000
# Population which looks at hygiene 10% of total population.
M = N * .1
# Initial number of infected and recovered individuals, I0 and R0.
# Decrease the infections number by 10%.
I0, R0 = 1 * .1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - M - I0 - R0
# Exposure:
# e.g. https://www.sciencedirect.com/science/article/pii/S1755436513000546
# Decrease by 10% because of hygiene.
E0 = .9
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.2, 1. / 10
# transmission rate, alpha and per-capita birth or death rate, mu.
# e.g. https://pubmed.ncbi.nlm.nih.gov/32087775/#:~:text=The%20microbiologically%20confirmed%20symptomatic%20transmission,21%20of%20119%20household%20members).
# e.g. https://bmcinfectdis.biomedcentral.com/articles/10.1186/s12879-019-4007-2#:~:text=A%20systematic%20review%20of%2039,per%20100%2C000%20persons%20%5B21%5D.
# Decrease alpha by 10% from 10% to 9%.
alpha, mu = .09, 3.2 / 100000
# A grid of time points (in days)
t = np.linspace(0, 80, 80)

# The SEIR model differential equations.
def deriv(y, t, N, alpha, beta, gamma, mu):
    S, E, I, R, = y
    dSdt = mu * N - beta * S * I - mu * S
    dEdt = beta * S * I - alpha * E - mu * E
    dIdt = alpha * E - gamma * I - mu * I
    dRdt = gamma * I - mu * R
    return dSdt, dEdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, E0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, alpha, beta, gamma, mu))
S, E, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S / 1000, 'b', alpha=.5, lw=2, label='Susceptible')
ax.plot(t, E / 1000, 'k', alpha=.5, lw=2, label='Exposure')
ax.plot(t, I / 1000, 'r', alpha=.5, lw=2, label='Infected')
ax.plot(t, R / 1000, 'g', alpha=.5, lw=2, label='Recovered with immunity')
ax.set_title('SEIR Model: Norovirus - with intervention')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0, 1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(visible=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()
del E, E0, I, I0, N, R, R0, S, S0, alpha, ax, beta, fig, gamma, legend, mu, ret, spine, t, y0