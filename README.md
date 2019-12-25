``` python
input_str = '''
a <- 1
print(c(1, 2))
if(a > 2) {
    print("a>2")
} else {
    print(c("a<2"))
    while(a < 5) {
        a <- a + 1  
        print(a)
     }
    matrix1 <- matrix(c(3, 9, -1, 4, 2, 6), nrow = 2, ncol = 3)
    print(matrix1)
    matrix2 <- matrix(c(5, 2, 0, 9, 3, 4), nrow = 2, ncol = 3)
    print(matrix2)
    result <- matrix1 + matrix2
    print(result)
}
m <- matrix(c(2, 6, 8), nrow=2, ncol=0, byrow=True)
print(m)
a = 3
print(class(322))
b = 4
a = c(2, 5, 6)
print(a)
print(c(1, 2, 5))
print(c(1, 2, 5) + c(1, 2, 5) / c(2, 2, 2))
print((c(1, 2, 5) + c(1, 2, 5)) / c(2, 2, 2))
ma = matrix(c(1, 3, 5), nrow=2, ncol=0, byrow=True)
print(ma)
print(ma + ma)
print(ma + ma - ma)
print(ma * ma)

# Create data for the graph.
x <- c(21, 62, 10, 53)
labels <- c("London", "New York", "Singapore", "Mumbai")
# Give the chart file a name.
png(file = "city_title_colours.png")
# Plot the chart with title and rainbow color pallet.
pie(x, labels, main = "City pie chart", col = rainbow(length(x)))
# Save the file.
dev.off()

# Create data for the graph.
v <- c(9,13,21,8,36,22,12,41,31,33,19)
# Give the chart file a name.
png(file = "histogram_lim_breaks.png")
# Create the histogram.
hist(v,xlab = "Weight",col = "green",border = "red", xlim = c(0,40), ylim = c(0,5), breaks = 5)
# Save the file.
dev.off()

H <- c(7,12,28,3,41)
M <- c("Mar","Apr","May","Jun","Jul")
# Give the chart file a name.
png(file="./barchart_months_revenue.png")
# Plot the bar chart.
barplot(H, names.arg=M, xlab="Month", ylab="Revenue", col="blue", main="Revenue chart", border="red")
dev.off()

# Create the data for the chart.
v <- c(7,12,28,3,41)
# Give the chart file a name.
png(file = "line_chart.png")
# Plot the bar chart. 
plot(v,type = "o")
# Save the file.
dev.off()
'''
```

