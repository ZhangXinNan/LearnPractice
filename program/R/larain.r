
# 安装TSA
# install.packages("TSA")
library(TSA)

data(larain)
# windows
win.graph(width = 4.8, height = 2.5, pointsize = 8)
# mac
# dev.new()

plot(larain, ylab = "Inches", xlab = "Year", type = "1", col = "black")
points(larain, col = "blue")
savePlot(filename = "LA_1.eps", type = c("eps"))

win.graph(width = 8, height = 8, pointsize = 8)
plot(y = larain, ylab = "Inches", xlab = "Year", type = "1", col = "black")
