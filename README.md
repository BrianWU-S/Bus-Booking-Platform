# Bus-Booking-Platform
A customized Bus-Booking platform. It provides economical service with real-time flexible route planning and order dispatch, which contributes to a better user experience.
## Introduction
Unlike car-hailing platforms, a bus-booking platform can dispatch several
passenger orders to one bus together, compute a specially planned route cycle based on these
requirements, and then ride the passengers to their destinations sequentially. Compared to carhailing, bus-booking can effectively utilize vehicle resources, reduce energy consumption, and save
road resources. Simultaneously, passengers could be served quickly with much lower price. In
all, combining the benefits of bus service and car-hailing, this new APP provides economical
service with real-time flexible route planning and order dispatch, which contributes to a better
user experience.
## Architecture Overview
* Destination selection 
* Order dispatch
* Route planning
* Pricing strategy for tickets
* Theoretical Analysis
## Brief Explanation
* Destination selection --> There are too many and flexible destinations for passengers,
so we identify a set of hot destinations as our “stations”. This simplification makes
passengers can only choose one of them as their destinations, instead of pointing an arbitrary location.
* Order dispatch --> We design a strategy to schedule passengers to different buses to minimize the number of buses while still meeting the needs of passengers
* Route planning --> Plan the route for each bus, so that we can help the company use minimum energy consumption and vehicle resource to earn maximum profit.
* Pricing strategy --> We design a bus fare rule system to attract as many passengers as possible while at the same time make 
as much profit as possible.

Note that the bus route is a cycle that starts from a departure station and returns back to this station again.
