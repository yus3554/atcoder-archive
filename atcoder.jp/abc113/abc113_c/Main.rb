N, M = gets.split.map { |e| e.to_i }
PY = []

M.times {|i|
    pTemp, yTemp = gets.split.map { |e| e.to_i }
    PY.push([pTemp, yTemp, i])
}

PY.sort! {|a, b| a[1] <=> b[1]}

index = []
N.times {
    index.push(0)
}

M.times {|i|
    index[PY[i][0] - 1] += 1
    PY[i][1] = index[PY[i][0] - 1]
}

PY.sort! {|a, b| a[2] <=> b[2]}

M.times {|i|
    puts format('%06d%06d', PY[i][0], PY[i][1])
}