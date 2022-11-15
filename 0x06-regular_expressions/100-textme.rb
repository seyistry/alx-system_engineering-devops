#!/usr/bin/env ruby
puts ARGV[0].scan(/.+from:([a-zA-Z0-9\+]+).+to:([a-zA-Z0-9\+]+).+flags:([\d\:\-]+).+/).join