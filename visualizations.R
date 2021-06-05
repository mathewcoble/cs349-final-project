library(tidyverse)
library(lubridate)
confirmed <- read_csv("COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
confirmed <- confirmed %>% pivot_longer(!c(`Province/State`, `Country/Region`, Lat, Long), names_to = "date", values_to = "cases")
confirmed <- confirmed %>% mutate(date = mdy(date))



confirmed %>% filter(str_starts(`Country/Region`, "Afghanistan")) %>% 
  ggplot(aes(x = date, y = cases, color = `Country/Region`)) +
  geom_point() +
  theme_minimal()

confirmed %>% filter(str_starts(`Country/Region`, "Belarus")) %>% 
  ggplot(aes(x = date, y = cases, color = `Country/Region`)) +
  geom_point() +
  theme_minimal()

confirmed %>% filter(str_starts(`Country/Region`, "US")) %>% 
  ggplot(aes(x = date, y = cases, color = `Country/Region`)) +
  geom_point() +
  theme_minimal()

confirmed %>% filter(str_starts(`Country/Region`, "Trini")) %>% 
  ggplot(aes(x = date, y = cases, color = `Country/Region`)) +
  geom_point() +
  theme_minimal()
