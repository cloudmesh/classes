.. add info about Globus Online (GridFTP)

GridFTP is a enhancement on the File Tranfer Protocol (FTP) which
provides high-performance , secure and reliable data transfer for
high-bandwidth wide-area networks. As noted in
:cite:`www-GlobusOnline` the most widely used implementation of
GridFTP is Globus Online. GridFTP achieves efficient use of
bandwidth by using multiple simultaneous TCP streams.  Files can
be downloaded in pieces simultaneously from multiple sources; or
even in separate parallel streams from the same source. GridFTP
allows transfers to be restarted automatically and handles
network unavailability with a fault tolerant implementation of
FTP.The underlying TCP connection in FTP has numerous settings
such as window size and buffer size. GridFTP allows automatic (or
manual) negotiation of these settings to provide optimal transfer
speeds and reliability .


