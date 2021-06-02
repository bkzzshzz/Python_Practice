# First about markdown. I think this text is enlarged.
#### Markdown is a type of formatting that allows the usage of various special characters to a lot of different purposes. 
To italic, insert the word between asterisks or two underscores. This is _italic_ or *italic*. 
To bold, insert the word between double asterisks or double underscores. This is __bold__ or **bold**. 
To strikethrough, insert the word between two tildes(~). This is ~~strikethrough~~. 

# Reference
#### Reference simply means address to a memory location. The following example can explain the about the difference in passing by value and passing by reference. 
    a = [1, 2, 3]
    b = a
    b.append(4)
    print (a)

Here the output will be **[1, 2, 3, 4]**. Why? Because what the second line actually does is not pass the value but pass the address or reference of the memory of _a_. This way, any change in _b_ will bring about the same change in _a_ as they share the same memory address. 

To counter this, there is the **list_name.copy()**. This only passes the values inside the list. 

    a = [1, 2, 3]
    b = a.copy()
    b.append(4)
    print (a)
Here, the output will be **[1, 2, 3]**.

##### The 'equals to' sign passes address. 






