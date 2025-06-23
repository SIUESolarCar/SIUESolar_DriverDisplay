def PixelToBytes(Pixels):
    Bytes = Pixels * 2 # 16 bits/2 Bytes per Pixel
    return Bytes

def LineChunker(File, ChunkWidth, SeekPoint):
    File.seek(SeekPoint)
    ChunkWidth = PixelToBytes(ChunkWidth)
    Chunk = bytearray(File.read(ChunkWidth))
    
    return Chunk

def Chunker(File, Index, ChunksInImage, ChunkWidth, ChunkHeight):
    FullChunk = b''
    for Line in range(ChunkHeight):
        SeekPoint = (Index * ChunkWidth) + (ChunksInImage * ChunkWidth) * Line
        FullChunk = FullChunk + LineChunker(File, ChunkWidth, SeekPoint)

    return FullChunk


data = open('Cyan.bin', 'rb')

ChunksInImage = 3 # How many images in the bin
ChunkWidth = 128 # Pixels
ChunkHeight = 64 # Pixels

Cyan =  Chunker(data, 0, 6, 128, 64)



