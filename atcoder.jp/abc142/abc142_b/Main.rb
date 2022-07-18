N, K = gets.split.map { |e| e.to_i }
h = gets.split.map { |e| e.to_i }

ans = 0

h.each do |i|
  if i >= K then
    ans += 1
  end
end

p ans
