# Short Polling
- periodic polling API, backend replies immediately (wastes requests)
# Long Polling
- periodic polling, backend hangs until new info or expiry after some time
# Server-sent events
- initial request which is long lived as server streams data to client
- LLMs for incremental progress
```
{
	'Content-Type': 'text/event-stream',
	'Connection': 'keep-alive',
	'Cache-Control': 'no-cache'
}

res.write(`data: thing`)
```
# Websockets
- bidirectional client-server communication protocol
- Authentication and authorization should work the same
- Ensure all users in room have same info
# Webhooks
- API request that fires to predetermined URL when event on source system occurs
	- Email opened in Sendgrid
- Source system does not know your system, so wehbook payload format is dependent on source
- Testing webhooks by tunneling dev server to internet with ngrok, cloudflare tunnels
- Authenticate webhooks with HMAC Signature verification, essentially a hash to compare to
# WebRTC
- p2p protocol between 2 machines to broadcast and receive video, audio, or screen sharing
- More than 2 people
	- Mesh
		- Each user connects to each other user, instead of sending 1 message, a user sends the same to each connection $n - 1$ times
		- Easy but not scalable and unstable
	- Multipoint Conferencing Unit (MCU)
		- Each user sends audio/video stream to a backend which combines everything and sends to user
		- Requires least bandwidth but hard to implement and need to encode/decode streams backend
	- Selective Forwarding Unit (SFU)
		- Eacher user stream to backend, but processing all streams on client-side
		- Scalable, but dependent on client hardware for processing
# Collaborative Web Apps
- Conflicts in multi-user collaborations depending on internet speed
- Operational Transformation, server contains source of truth, good with text by auto adjusting changes to original intent
- Conflict-free Replicated Data Type (CRDT)