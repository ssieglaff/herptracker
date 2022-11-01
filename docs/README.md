# Herptracker User Stories
## User Stories
1. As a **site admin**, I want to **appoint and remove data admins** so they can **maintain and update herp data**.
2. As a **data admin**, I want to **record herps to the lowest taxonomic group** so I can **keep track of what kind of herps have been caught**.
3. As a **data admin**, I want to **record data about the herp (length of snake, weight of frog, etc)** so I can **track trends in herp phenotypes**.
4. As a **data admin**, I want to **record specific kinds of traps** so I can **keep track of which techniques observed which kinds of herps**.
5. As a **data admin**, I want to **record specific trap setting and checking times and locations** so I can **keep track of herp trends by trap type and timeline**.
6. As a **data admin**, I want to **record field data on a mobile device** so I can **input data easily and accurately**.
7. As a **user**, I want to **analyze weather data** so I can **compare weather trends to herp observation data**.
8. As a **user**, I want to **sort and filter the different herp captures** so I can **observe trends specific to species or other taxomomic group**.
9. As a **user**, I want to **perform various statistical calculations based on filtered datasets** so I can **express numerical data about herp activity**.
10. As a **user**, I want to **compose charts/graphs based on the the filtered dataset** so I can **visualize data about herp activity**.
## Acceptance Criteria
1. The web application must allow three heirerachical levels of access: site admin, data admin, and normal user.
2. The site admin needs to be able to appoint new data admins, update the herp database, and view/analyze the herp data.
3. The data admin needs to be able to update the herp database and view/analyze the herp data.
4. The normal user needs to be able to view/analyze the herp data.
5. The herp database needs to record types of herps that were found, including species name, taxonomic group, and size.
6. The herp database needs to record whether or not the herp was caught in a trap or just seen, and if it was trapped the time the trap was set and checked, and record all the herps that were found in that trap when checked.
7. The web application must pull weather data within user-specified time frames at user-specified locations from Weather Underground.
8. The web application must render a web page for the user that displays all the herp data in the database.
9. The web application must allow the user to sort and filter the herp data per each field of data.
10. The web application must take a user-selected subset of the herp data and calculate frequency, maximum value, minimum value, and average, as well as generate histograms, pie charts, and scatterplots.
## Mis-user Stories
1. As a user, I want to add and edit the herp data so I can generate fraudulent herp statistics.
2. As a user, I want to revoke data admins so I can deny service to updating the herp data.
3. As a user, I want to flood the webapp with requests so I can deny service to accessing the herp data.
4. As a user, I want to generate graphs with misleading axis or labels so I can commit data fraud.
5. As a data admin, I want to repudiate my activity with the herp data so I can avoid blame for creating fraudulent data.
## Mitigation Criteria
1. Users must log in with site or data admin credentials to be able to update the herp database.
2. Users must log in with site admin credentials to appoint or revoke data admin privelege.
3. The web app will allow a user to submit at most one request to the database within a 15-second window.
4. The web app will only allow the user to select from a list of predetermined graphical representation options when generating data visuals.
5. The web app will log all database transactions with the date, time, and username of the user who performed the transaction.