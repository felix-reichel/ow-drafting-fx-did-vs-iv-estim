# ow-drafting-fx-did-vs-iv-estim
Using covid-19 **non-drafting** response policies (\~2020-2022) for estimating the magnitude of swim drafting benefits (\~ >20% according to sports literature)

## Research Questions

1. Does the according to literature 20\% drafting benefit $\implies$ 20\% better mean outcomes in drafting races? 

[did_pic.pdf](https://github.com/user-attachments/files/17090156/did_pic.pdf)

2. Effect heterogenity: Which groups (e.g. percentiles) benefit the most from drafting? Marginal effects, ...


## Research Design

### A Simple Difference-in-Differences (DID) Model with Three Periods:

A simple DiD regression formula with Three Periods reads:

$$
Y_{it} = \gamma_0 + \gamma_1 \mathbb{1}_{\{t \in \text{COVID}\}}
$$

$$
+\gamma_2 \mathbb{1}_{\{t \in \text{PostCOVID}\}}
$$

$$
+\gamma_3 \mathbb{1}_{\{i \in \text{Drafting}\}}
$$

$$
+\gamma_4 \mathbb{1}_{\{t \in \text{COVID}\}}
$$

$$
\times \mathbb{1}_{\{i \in \text{Drafting}\}}
$$

$$
+\gamma_5 \mathbb{1}_{\{t \in \text{PostCOVID}\}}
$$

$$
\times \mathbb{1}_{\{i \in \text{Drafting}\}}
$$

$$
+\mu_i + \nu_j + \delta_t + \theta_t \text{Trend} + \varepsilon_{it}
$$

Where:

- $Y_{it}$ : Outcome variable; Swim time for athlete $i$ at time $t$.
- $\gamma_0$: Intercept; Baseline outcome.
- $\mathbb{1}_{\{t \in \text{COVID}\}}$: Indicator (dummy) variable equal to 1 if time $t$ is during the COVID period (2020–2022), and 0 otherwise.
- $\mathbb{1}_{\{t \in \text{PostCOVID}\}}$: Indicator variable equal to 1 if time $t$ is during the Post-COVID period (post-2022), and 0 otherwise.
- $\mathbb{1}_{\{i \in \text{Drafting}\}}$: Indicator variable equal to 1 if athlete $i$ is in the drafting (allowed) group (**exposed to group starts and has *ENHANCED* drafting ability**), and 0 otherwise.
- $\gamma_4 ...$  Interaction term representing the effect of the COVID period (no drafting) on treated athletes.
- $\gamma_5 ...$ Interaction term representing the effect of the Post-COVID period (drafting reinstated) on treated athletes.
- $\mu_i$: Athlete FE; time-invariant characteristics specific to each athlete.
- $\nu_j$: Event FE
- $\delta_t$: Seasonal/Month FE; for general seasonality; Mesozyklus and Misozyklus, Build/Maintain/Peak Phase in training.
- $\theta_t \text{Trend}$: A time trend to control for general performance improvements over time (such as technology or training advancements).
- $\varepsilon_{it}$: Error term.

## with Three Periods:

1. **Pre-COVID (Baseline)**: No restrictions on drafting. This is the reference period, so no indicator variable is needed for this period.
2. **COVID Non-Drafing response policy (2020–2022)**: Single starts with no drafting allowed, represented by $\mathbb{1}_{\{t \in \text{COVID}\}}$.
3. **Post-COVID (Post-2022)**: Group starts reinstated, allowing drafting again, represented by $\mathbb{1}_{\{t \in \text{PostCOVID}\}}$.


## Data Requirements
