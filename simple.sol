// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract Simplestorage {
    uint256 favno;
    bool favbool;
        int256 op;
        string name;
    // bool favbool2;

    struct People {
        string name;
        uint256 favno;
    }
    // People public person = People({favno: 7, name: "Kshitiz"});

    People[] public peopl;
    mapping(string =>uint256)public nameTofavno;

    address fav = 0xA44c7b5B7dEb84209855E62e460C7F0e884F5887;

    function store(uint _favno) public {
        favno =_favno;
    op = 10;
    name = "ksj";
    }

    // function retrive() public view returns (uint256,int256,string memory){
    //     return (favno,op,name);
    // }


    //  function retrie() public view returns (string memory) {
    //     return name;
    // }

    //  function retrve() public view returns (int256) {
    //     return op ;
    // }
    function addPerson(string memory _name, uint256 _favno) public {
        peopl.push(People({favno: _favno, name: _name}));
        nameTofavno[_name]=_favno;
    }
}
