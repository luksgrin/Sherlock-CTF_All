pragma solidity 0.7.6;

contract Probaso {

    event averlo(bytes _data);
    event averlo2(bytes32 _data);

    constructor () {
    }

    fallback() external payable {

        bytes memory lolardo = abi.encodePacked(bytes28(0), msg.data);

        (bytes32 sig, bytes32 data) = abi.decode(lolardo, (bytes32,bytes32));
        emit averlo(lolardo);
        emit averlo2(data);
     }
}
