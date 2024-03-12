const ethers = require('ethers');

// Use Infura or any other provider
const provider = new ethers.JsonRpcProvider('http://94.237.49.182:54163');
//const provider = new ethers.providers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY');

// The private key and address you provided
const privateKey = '0x4e30a42cc868ce8ae52fa9b8d7d0fcad9af5d5fe6ba1510fdaa6ef74bf6ecb80';
const wallet = new ethers.Wallet(privateKey, provider);


// RussianRoulette contract information (Adjust ABI and address as necessary)
const russianRouletteABI = [
    {
      "inputs": [],
      "name": "pullTrigger",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ] // ABI for RussianRoulette
const russianRouletteAddress = '0xaa6767e4cB586D8f689144C982AB7A832b05Ce30';
const russianRouletteContract = new ethers.Contract(russianRouletteAddress, russianRouletteABI, wallet);

async function playRussianRoulette() {
    try {
        // Call the pullTrigger function
        let tx = await russianRouletteContract.pullTrigger();
        await tx.wait();
        console.log('Transaction completed:', tx.hash);

        // After executing, check if the Setup contract's condition is met (Optional)
        // You would need to interact with the Setup contract in a similar manner

    } catch (error) {
        console.error('Error playing Russian Roulette:', error);
    }
}

playRussianRoulette();
