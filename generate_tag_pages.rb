require 'yaml'
require 'fileutils'

# Path to your posts
def posts_dir
  Dir.exist?("_posts") ? "_posts" : "posts"
end
# Path to output tag pages
tags_dir = "tags"

FileUtils.mkdir_p(tags_dir)

tags = Hash.new { |h, k| h[k] = [] }

# Collect tags from all posts

require 'date'
Dir.glob("#{posts_dir}/*.md") do |post_file|
  content = File.read(post_file)
  if content =~ /---(.*?)---/m
    front_matter = Psych.safe_load($1, permitted_classes: [Date], aliases: true)
    if front_matter["tags"]
      tags_field = front_matter["tags"]
      if tags_field.is_a?(Array)
        tags_field.each { |tag| tags[tag] << post_file }
      elsif tags_field.is_a?(String)
        tags[tags_field] << post_file
      end
    end
  end
end

# Generate a .md file for each tag
tags.keys.each do |tag|
  File.open("#{tags_dir}/#{tag}.md", "w") do |f|
    f.puts <<~TAGPAGE
      ---
      layout: tag
      title: "Tag: #{tag}"
      tag: #{tag}
      permalink: /tags/#{tag}/
      ---
    TAGPAGE
  end
end

puts "Generated tag pages for: #{tags.keys.join(', ')}"
