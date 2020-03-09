# Downloading the libraries necessary for data anlysis and plotting
library(dplyr)
library(ggplot2)

### LOOKING AT LOW INCOME VS DISTANCE

# filter dataset so that it only include low income census tracts
low_income <- filter(food_access_data, low_income_flag == 1)
head(low_income) 
# select data to exclude race and look at totals
# based on already-filtered dataset
LowInc <- select(low_income, low_income_flag, total_half, total_1, total_10, total_20)
head(LowInc)

# calculate percent low income at every distance from supermarket
TotalHalf <- sum(LowInc$total_half)
Total1 <- sum(LowInc$total_1)
Total10 <- sum(LowInc$total_10)
Total20 <- sum(LowInc$total_20)
Totals <- select(food_access_data, total_half, total_1, total_10, total_20)
head(Totals)
total_half <- sum(food_access_data$total_half)
total_1 <- sum(food_access_data$total_1)
total_10 <- sum(food_access_data$total_10)
total_20 <- sum(food_access_data$total_20)
perc_low_half <- TotalHalf/total_half * 100
perc_low_1 <- Total1/total_1 * 100
perc_low_10 <- Total10/total_10 * 100
perc_low_20 <- Total20/total_20 * 100

# Bar graph #1
low_income_bar <- c(perc_low_half, perc_low_1, perc_low_10, perc_low_20)
low_income_bar
bar_low <- barplot(low_income_bar, col=rgb(0.2,0.4,0.6,0.6)) 

# Specific color for each bar
library(RColorBrewer)
coul <- brewer.pal(5, "Set2") 
LowBar <- barplot(low_income_bar, 
        col=coul, 
        xlab="Distance (miles)", 
        names.arg=c("0.5", "1", "10", "20"),
        ylab="Percent Low Income", 
        main="Percent Low Income VS Distance from Supermarket", 
        ylim=c(0,60)
)

# Use ggplot2
df <- data.frame(distance = c(0.5, 1, 10, 20), low_income_bar)
ggplot(df, aes(distance, low_income_bar)) + geom_bar(stat = "identity", fill = "navyblue")

# Use ggplot2 --> Treat distance like a string for better visualization
# fill/color = maroon
df <- data.frame(distance = c("0.5", "1", "10", "20"), low_income_bar)
ggplot(df, aes(distance, low_income_bar)) + 
        geom_bar(stat = "identity", fill = "maroon") + 
        ggtitle("Percent Low Income VS Distance from the Supermarket") +
        xlab("Distance (miles)") +
        ylab("Low Income Population (%)")

# modify plot color --> Blues palette
df <- data.frame(distance = c("0.5", "1", "10", "20"), low_income_bar)
# need to have "fill=distance" in order for palette to apply!
# dicrete variable will be filled
ggplot(df, aes(distance, low_income_bar, fill = distance)) + 
        # "stat=identity" makes the x axis discrete
        geom_bar(stat = "identity") + 
        scale_fill_brewer(palette = "Blues") +
        ggtitle("Percent Low Income VS Distance from the Supermarket") +
        xlab("Distance (miles)") +
        ylab("Low Income Population (%)")

display.brewer.all()

### NOW LOOKING AT VEHICLE ACCESS VS DISTANCE
# filter dataset so that it only include low vehicle access census tracts
vehicle <- filter(food_access_data, low_vehicle_access_flag == 1)
head(vehicle) 
# select data to exclude race and look at totals
LowVehicle <- select(vehicle, low_vehicle_access_flag, total_half, total_1, total_10, total_20)
head(LowVehicle)

# calculate percent low income at every distance from supermarket
VTotalHalf <- sum(LowVehicle$total_half)
VTotal1 <- sum(LowVehicle$total_1)
VTotal10 <- sum(LowVehicle$total_10)
VTotal20 <- sum(LowVehicle$total_20)
# Totals from food_acess_data have already been defined
Vperc_low_half <- VTotalHalf/total_half * 100
Vperc_low_1 <- VTotal1/total_1 * 100
Vperc_low_10 <- VTotal10/total_10 * 100
Vperc_low_20 <- VTotal20/total_20 * 100

# ggplot2 to create barplot
df2 <- data.frame(distance = c("0.5", "1", "10", "20"), vehicle_bar = c(Vperc_low_half, Vperc_low_1, Vperc_low_10, Vperc_low_20))
ggplot(df2, aes(distance, vehicle_bar, fill = distance)) + 
        # "stat=identity" makes the x axis discrete
        geom_bar(stat = "identity") + 
        scale_fill_brewer(palette = "Reds") +
        ggtitle("Percent Low Vehicle Access VS Distance from the Supermarket") +
        xlab("Distance (miles)") +
        ylab("Population with Low Vehicle Access (%)")
