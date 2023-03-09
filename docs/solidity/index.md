# mapping dont have key

* I just use another mapping to map an address like a link starts with  0x0000000000000000000000000000000000000000
* The Key 0x0000000000000000000000000000000000000000 got the value of some address
* If the address is not found in the the map it always returns default value
* That is 0x0000000000000000000000000000000000000000

```ruby
0 -> a
a -> b
b -> c
c -> 0
```

```solidity
struct Customer {
  string name;
  string email;
}

mapping(address => Customer) customer;
mapping(address => address) IDs; // this is the map that make a link address by address or (foo by foo)

function addCustomer(string memory _name, string memory _email) public {
  address tmp;
  tmp = IDs[0x0000000000000000000000000000000000000000];
  do{
    if(IDs[tmp] == 0x0000000000000000000000000000000000000000){
      IDs[tmp] == msg.sender;
      customer[msg.sender] =  Customer({name:_name, email:_email});
      break;
    }
    tmp = IDs[tmp];
  }while (true);
}
```
