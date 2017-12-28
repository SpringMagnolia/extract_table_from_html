# 从网页中提取table中的数据
#### 最近遇到一个问题，table中的数据，如何快速的提取出来，记得pandas有个方法read_html，看了下源码能够使用正则匹配页面的所有table
#### 所以写了个方法，使用requests来请求，使用xpath提取包含table的页面字符串，传递个pandas的read_html，转化为DataFrame，然后转化为列表