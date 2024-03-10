<Query Kind="Program" />

class Program
{	
    static void Main(string[] args)
    {
		var startChar = 0;
		var text = new byte[4096];
		
        var data = File.ReadAllBytes(@"message.txt.cz");
		//var data = File.ReadAllBytes(@"test.cz");

		int position = 0;
		int iteration = 0;

		for (int i = position; i < data.Length; i += 8)
		{
			if (data.Length < i + 8) break;

			var charListLength = data[i];

			for (int j = 0; j < charListLength * 8; j += 8)
			{
				var index = BitConverter.ToInt64(data, i + 8);
				text[index] = (byte)(startChar + iteration);
				i += 8;
			}

			position = i;
			iteration++;
		}

		Encoding.ASCII.GetString(text).Dump();
	}
}
