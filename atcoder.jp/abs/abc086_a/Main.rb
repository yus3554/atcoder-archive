a, b = gets.split.map{|v| v.to_i}

puts a * b % 2 == 0 ? "Even" : "Odd"
