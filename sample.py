from Crypto.Cipher import AES
from binascii import unhexlify

key = b'24305c3a354951afe96d1800ad9299bf'

iv = b'heF9BATUfWuISyO8'
data= unhexlify(b'48fcbd0c1e1643bd618c010e57142a1e45c7fd5e36374eb1738f5b9ab6b4ce67bfea3e226426d43a2aaf9140eced8547d7a6199bde167a9e20de0a87f5c9a9a34361dce8d1d8c35a00018895c200bedebf24c30c920c134e5f956d1dfd1201abc3410c093adae070d7771bb5f99145351620573e6fff748ee3b260c9c2a483b886f331497c4023eb370ad1f881a4d165bf5cc8eb9e4008529e6ad2b759767c4cd65f764ffd6412fb58ce5914e2a5280024ac353b5d3b69707afe0c2ad138ffa85b712de22fb84ff2276fe360d6f87abc7879c3e592ec36055da14952eb0c1c973d8f55bd4b662593875b29b83be90b2b4f944b1ed036d4d2e3912ab11c42f77444c93e94d953023a27e8dbd24d7df17c27de5f0bf1ad334d833a8fa78d7ffc85179dc1ade4c32ced6bd902e8ddedad7305db5d2d1e33e5d96cb4422b4dc8f9ab6bb1e88685c44f6bfcc97d1d6b59ab96578c443103f5d4ae72b4cf09a87935e217ae9457a37433b97f6ba7700e1c5960cfefd255f0c740259f8e3c0ac8e9bee82b36742f5922d14964015dce9b2a8a014494821a98224811f2649e92d0372603fd569103be7763065bb9bc2a6a08a9f8da0ce1b567028ae41b83a8e2d19f6f98e22290aaca549c25318cd57f85b0dd9fde9c93f9f790b93a3f4f1787c34382b2b3b9190702723a1fd451c0e285b9258bd6e89b6bf3682760b1273c1a5c7781bac7db9c024e981099181b03c8f85ce0accfa4e1448539b1b62733192a8e2cf98741cfc60e13753c4ca55b26a40fdf0616445a9a46428adc0852c5c84d0a3878ee32f3d1b88cf7cf19a58bb69fb3f4cc43baa67012cc1947da6c0253c9cc291cfcc721faf0e3c16e738c52b94308d7c51a6bc929b8b106dfe546066215a84d410644d5bc6a4b5feae10a377ec57ca3ddce6073aa6f7e968ef97ac1e52a449c1290aa06442e8c15e0aef8d75a6348a3be2869fd90a944867ea7779c01530f73170adf5509fbf3600825758f85372afedb56')

data1=unhexlify(b'8d438cfe60b832b10935489c845d9fd8d2a36d09fd375413ddc8172fa7d60221')
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original_data = (cipher.decrypt(data), AES.block_size)
print(original_data)
#print(original_data.decrypt(data.decode('hex')))