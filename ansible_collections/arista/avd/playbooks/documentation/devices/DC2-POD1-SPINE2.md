# DC2-POD1-SPINE2
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)
- [EOS CLI](#eos-cli)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | mgmt | 10.6.65.11/24 | 10.6.65.1 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | oob_management | oob | mgmt | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management0
   description oob_management
   no shutdown
   vrf mgmt
   ip address 10.6.65.11/24
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS |
| ---- | ----- |
| False | True |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| mgmt | - | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf mgmt
      no shutdown
```

# Authentication

## Local Users

### Local Users Summary

| User | Privilege | Role |
| ---- | --------- | ---- |
| admin | 15 | network-admin |

### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 $6$82gqIqw8b3nibNrk$MoZO0S8QMQN8uwnR8v48dbGrL0Ec/6q36tSx8y9IsExi4L.HtmokW9rX8VehLxhg542mNTBKqxMBF.LgnCTm4.
```

# Monitoring

## SNMP

### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | AMS DC2 DC2_POD1 DC2-POD1-SPINE2 | All | Disabled |

### SNMP Device Configuration

```eos
!
snmp-server location AMS DC2 DC2_POD1 DC2-POD1-SPINE2
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **none**

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1/1 | P2P_LINK_TO_DC2-POD1-LEAF1A_Ethernet30/1 | routed | - | 172.17.64.154/31 | default | 9214 | false | - | - |
| Ethernet2/1 | P2P_LINK_TO_DC2-POD1-LEAF1B_Ethernet30/1 | routed | - | 172.17.64.162/31 | default | 9214 | false | - | - |
| Ethernet3/1 | P2P_LINK_TO_DC2-POD1-LEAF2A_Ethernet30/1 | routed | - | 172.17.64.178/31 | default | 9214 | false | - | - |
| Ethernet4/1 | P2P_LINK_TO_DC2-POD1-LEAF2B_Ethernet30/1 | routed | - | 172.17.64.186/31 | default | 9214 | false | - | - |
| Ethernet5/1 | P2P_LINK_TO_DC2-POD1-LEAF3A_Ethernet30/1 | routed | - | 172.17.64.194/31 | default | 9214 | false | - | - |
| Ethernet6/1 | P2P_LINK_TO_DC2-POD1-LEAF3B_Ethernet30/1 | routed | - | 172.17.64.202/31 | default | 9214 | false | - | - |
| Ethernet7/1 | P2P_LINK_TO_DC2-POD1-LEAF4A_Ethernet30/1 | routed | - | 172.17.64.210/31 | default | 9214 | false | - | - |
| Ethernet8/1 | P2P_LINK_TO_DC2-POD1-LEAF4B_Ethernet30/1 | routed | - | 172.17.64.218/31 | default | 9214 | false | - | - |
| Ethernet9/1 | P2P_LINK_TO_DC2-POD1-LEAF5A_Ethernet30/1 | routed | - | 172.17.64.226/31 | default | 9214 | false | - | - |
| Ethernet10/1 | P2P_LINK_TO_DC2-POD1-LEAF5B_Ethernet30/1 | routed | - | 172.17.64.234/31 | default | 9214 | false | - | - |
| Ethernet11/1 | P2P_LINK_TO_DC2-POD1-LEAF6A_Ethernet30/1 | routed | - | 172.17.64.242/31 | default | 9214 | false | - | - |
| Ethernet12/1 | P2P_LINK_TO_DC2-POD1-LEAF6B_Ethernet30/1 | routed | - | 172.17.64.250/31 | default | 9214 | false | - | - |
| Ethernet13/1 | P2P_LINK_TO_DC2-POD1-LEAF7A_Ethernet30/1 | routed | - | 172.17.65.2/31 | default | 9214 | false | - | - |
| Ethernet14/1 | P2P_LINK_TO_DC2-POD1-LEAF7B_Ethernet30/1 | routed | - | 172.17.65.10/31 | default | 9214 | false | - | - |
| Ethernet15/1 | P2P_LINK_TO_DC2-POD1-LEAF8A_Ethernet30/1 | routed | - | 172.17.65.18/31 | default | 9214 | false | - | - |
| Ethernet16/1 | P2P_LINK_TO_DC2-POD1-LEAF8B_Ethernet30/1 | routed | - | 172.17.65.26/31 | default | 9214 | false | - | - |
| Ethernet17/1 | P2P_LINK_TO_DC2-POD1-LEAF9A_Ethernet30/1 | routed | - | 172.17.65.34/31 | default | 9214 | false | - | - |
| Ethernet18/1 | P2P_LINK_TO_DC2-POD1-LEAF9B_Ethernet30/1 | routed | - | 172.17.65.42/31 | default | 9214 | false | - | - |
| Ethernet19/1 | P2P_LINK_TO_DC2-POD1-LEAF10A_Ethernet30/1 | routed | - | 172.17.65.50/31 | default | 9214 | false | - | - |
| Ethernet20/1 | P2P_LINK_TO_DC2-POD1-LEAF10B_Ethernet30/1 | routed | - | 172.17.65.58/31 | default | 9214 | false | - | - |
| Ethernet21/1 | P2P_LINK_TO_DC2-POD1-LEAF11A_Ethernet30/1 | routed | - | 172.17.65.66/31 | default | 9214 | false | - | - |
| Ethernet22/1 | P2P_LINK_TO_DC2-POD1-LEAF11B_Ethernet30/1 | routed | - | 172.17.65.74/31 | default | 9214 | false | - | - |
| Ethernet23/1 | P2P_LINK_TO_DC2-POD1-LEAF12A_Ethernet30/1 | routed | - | 172.17.65.82/31 | default | 9214 | false | - | - |
| Ethernet24/1 | P2P_LINK_TO_DC2-POD1-LEAF12B_Ethernet30/1 | routed | - | 172.17.65.90/31 | default | 9214 | false | - | - |
| Ethernet25/1 | P2P_LINK_TO_DC2-POD1-LEAF13A_Ethernet30/1 | routed | - | 172.17.65.98/31 | default | 9214 | false | - | - |
| Ethernet26/1 | P2P_LINK_TO_DC2-POD1-LEAF13B_Ethernet30/1 | routed | - | 172.17.65.106/31 | default | 9214 | false | - | - |
| Ethernet27/1 | P2P_LINK_TO_DC2-POD1-LEAF14A_Ethernet30/1 | routed | - | 172.17.65.114/31 | default | 9214 | false | - | - |
| Ethernet28/1 | P2P_LINK_TO_DC2-POD1-LEAF14B_Ethernet30/1 | routed | - | 172.17.65.122/31 | default | 9214 | false | - | - |
| Ethernet29/1 | P2P_LINK_TO_SUPER-SPINE1_Ethernet10/1 | routed | - | 172.16.64.23/31 | default | 9214 | false | - | - |
| Ethernet30/1 | P2P_LINK_TO_SUPER-SPINE2_Ethernet10/1 | routed | - | 172.16.64.87/31 | default | 9214 | false | - | - |
| Ethernet31/1 | P2P_LINK_TO_SUPER-SPINE3_Ethernet10/1 | routed | - | 172.16.64.151/31 | default | 9214 | false | - | - |
| Ethernet32/1 | P2P_LINK_TO_SUPER-SPINE4_Ethernet10/1 | routed | - | 172.16.64.215/31 | default | 9214 | false | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_LINK_TO_DC2-POD1-LEAF1A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.154/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet2/1
   description P2P_LINK_TO_DC2-POD1-LEAF1B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.162/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet3/1
   description P2P_LINK_TO_DC2-POD1-LEAF2A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.178/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet4/1
   description P2P_LINK_TO_DC2-POD1-LEAF2B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.186/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet5/1
   description P2P_LINK_TO_DC2-POD1-LEAF3A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.194/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet6/1
   description P2P_LINK_TO_DC2-POD1-LEAF3B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.202/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet7/1
   description P2P_LINK_TO_DC2-POD1-LEAF4A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.210/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet8/1
   description P2P_LINK_TO_DC2-POD1-LEAF4B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.218/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet9/1
   description P2P_LINK_TO_DC2-POD1-LEAF5A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.226/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet10/1
   description P2P_LINK_TO_DC2-POD1-LEAF5B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.234/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet11/1
   description P2P_LINK_TO_DC2-POD1-LEAF6A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.242/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet12/1
   description P2P_LINK_TO_DC2-POD1-LEAF6B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.64.250/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet13/1
   description P2P_LINK_TO_DC2-POD1-LEAF7A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.2/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet14/1
   description P2P_LINK_TO_DC2-POD1-LEAF7B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.10/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet15/1
   description P2P_LINK_TO_DC2-POD1-LEAF8A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.18/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet16/1
   description P2P_LINK_TO_DC2-POD1-LEAF8B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.26/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet17/1
   description P2P_LINK_TO_DC2-POD1-LEAF9A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.34/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet18/1
   description P2P_LINK_TO_DC2-POD1-LEAF9B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.42/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet19/1
   description P2P_LINK_TO_DC2-POD1-LEAF10A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.50/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet20/1
   description P2P_LINK_TO_DC2-POD1-LEAF10B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.58/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet21/1
   description P2P_LINK_TO_DC2-POD1-LEAF11A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.66/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet22/1
   description P2P_LINK_TO_DC2-POD1-LEAF11B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.74/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet23/1
   description P2P_LINK_TO_DC2-POD1-LEAF12A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.82/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet24/1
   description P2P_LINK_TO_DC2-POD1-LEAF12B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.90/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet25/1
   description P2P_LINK_TO_DC2-POD1-LEAF13A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.98/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet26/1
   description P2P_LINK_TO_DC2-POD1-LEAF13B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.106/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet27/1
   description P2P_LINK_TO_DC2-POD1-LEAF14A_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.114/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet28/1
   description P2P_LINK_TO_DC2-POD1-LEAF14B_Ethernet30/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.17.65.122/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet29/1
   description P2P_LINK_TO_SUPER-SPINE1_Ethernet10/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.64.23/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet30/1
   description P2P_LINK_TO_SUPER-SPINE2_Ethernet10/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.64.87/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet31/1
   description P2P_LINK_TO_SUPER-SPINE3_Ethernet10/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.64.151/31
   ptp enable
   service-profile P2P-QOS-PROFILE
!
interface Ethernet32/1
   description P2P_LINK_TO_SUPER-SPINE4_Ethernet10/1
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.64.215/31
   ptp enable
   service-profile P2P-QOS-PROFILE
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 10.4.64.12/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 10.4.64.12/32
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | true |
| mgmt | false |

### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf mgmt
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | false |
| mgmt | false |

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| mgmt  | 0.0.0.0/0 |  10.6.65.1  |  -  |  1  |  -  |  -  |  - |

### Static Routes Device Configuration

```eos
!
ip route vrf mgmt 0.0.0.0/0 10.6.65.1
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 64802|  10.4.64.12 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- |
| 172.16.64.22 | 64501 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.64.86 | 64502 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.64.150 | 64503 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.16.64.214 | 64504 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.155 | 65101 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.163 | 65101 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.179 | 65102 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.187 | 65102 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.195 | 65103 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.203 | 65103 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.211 | 65104 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.219 | 65104 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.227 | 65105 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.235 | 65105 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.243 | 65106 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.64.251 | 65106 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.3 | 65107 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.11 | 65107 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.19 | 65108 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.27 | 65108 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.35 | 65109 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.43 | 65109 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.51 | 65110 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.59 | 65110 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.67 | 65111 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.75 | 65111 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.83 | 65112 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.91 | 65112 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.99 | 65113 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.107 | 65113 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.115 | 65114 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |
| 172.17.65.123 | 65114 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - |

### Router BGP Device Configuration

```eos
!
router bgp 64802
   router-id 10.4.64.12
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.64.22 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.64.22 remote-as 64501
   neighbor 172.16.64.22 description SUPER-SPINE1_Ethernet10/1
   neighbor 172.16.64.86 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.64.86 remote-as 64502
   neighbor 172.16.64.86 description SUPER-SPINE2_Ethernet10/1
   neighbor 172.16.64.150 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.64.150 remote-as 64503
   neighbor 172.16.64.150 description SUPER-SPINE3_Ethernet10/1
   neighbor 172.16.64.214 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.64.214 remote-as 64504
   neighbor 172.16.64.214 description SUPER-SPINE4_Ethernet10/1
   neighbor 172.17.64.155 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.155 remote-as 65101
   neighbor 172.17.64.155 description DC2-POD1-LEAF1A_Ethernet30/1
   neighbor 172.17.64.163 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.163 remote-as 65101
   neighbor 172.17.64.163 description DC2-POD1-LEAF1B_Ethernet30/1
   neighbor 172.17.64.179 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.179 remote-as 65102
   neighbor 172.17.64.179 description DC2-POD1-LEAF2A_Ethernet30/1
   neighbor 172.17.64.187 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.187 remote-as 65102
   neighbor 172.17.64.187 description DC2-POD1-LEAF2B_Ethernet30/1
   neighbor 172.17.64.195 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.195 remote-as 65103
   neighbor 172.17.64.195 description DC2-POD1-LEAF3A_Ethernet30/1
   neighbor 172.17.64.203 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.203 remote-as 65103
   neighbor 172.17.64.203 description DC2-POD1-LEAF3B_Ethernet30/1
   neighbor 172.17.64.211 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.211 remote-as 65104
   neighbor 172.17.64.211 description DC2-POD1-LEAF4A_Ethernet30/1
   neighbor 172.17.64.219 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.219 remote-as 65104
   neighbor 172.17.64.219 description DC2-POD1-LEAF4B_Ethernet30/1
   neighbor 172.17.64.227 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.227 remote-as 65105
   neighbor 172.17.64.227 description DC2-POD1-LEAF5A_Ethernet30/1
   neighbor 172.17.64.235 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.235 remote-as 65105
   neighbor 172.17.64.235 description DC2-POD1-LEAF5B_Ethernet30/1
   neighbor 172.17.64.243 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.243 remote-as 65106
   neighbor 172.17.64.243 description DC2-POD1-LEAF6A_Ethernet30/1
   neighbor 172.17.64.251 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.64.251 remote-as 65106
   neighbor 172.17.64.251 description DC2-POD1-LEAF6B_Ethernet30/1
   neighbor 172.17.65.3 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.3 remote-as 65107
   neighbor 172.17.65.3 description DC2-POD1-LEAF7A_Ethernet30/1
   neighbor 172.17.65.11 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.11 remote-as 65107
   neighbor 172.17.65.11 description DC2-POD1-LEAF7B_Ethernet30/1
   neighbor 172.17.65.19 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.19 remote-as 65108
   neighbor 172.17.65.19 description DC2-POD1-LEAF8A_Ethernet30/1
   neighbor 172.17.65.27 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.27 remote-as 65108
   neighbor 172.17.65.27 description DC2-POD1-LEAF8B_Ethernet30/1
   neighbor 172.17.65.35 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.35 remote-as 65109
   neighbor 172.17.65.35 description DC2-POD1-LEAF9A_Ethernet30/1
   neighbor 172.17.65.43 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.43 remote-as 65109
   neighbor 172.17.65.43 description DC2-POD1-LEAF9B_Ethernet30/1
   neighbor 172.17.65.51 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.51 remote-as 65110
   neighbor 172.17.65.51 description DC2-POD1-LEAF10A_Ethernet30/1
   neighbor 172.17.65.59 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.59 remote-as 65110
   neighbor 172.17.65.59 description DC2-POD1-LEAF10B_Ethernet30/1
   neighbor 172.17.65.67 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.67 remote-as 65111
   neighbor 172.17.65.67 description DC2-POD1-LEAF11A_Ethernet30/1
   neighbor 172.17.65.75 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.75 remote-as 65111
   neighbor 172.17.65.75 description DC2-POD1-LEAF11B_Ethernet30/1
   neighbor 172.17.65.83 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.83 remote-as 65112
   neighbor 172.17.65.83 description DC2-POD1-LEAF12A_Ethernet30/1
   neighbor 172.17.65.91 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.91 remote-as 65112
   neighbor 172.17.65.91 description DC2-POD1-LEAF12B_Ethernet30/1
   neighbor 172.17.65.99 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.99 remote-as 65113
   neighbor 172.17.65.99 description DC2-POD1-LEAF13A_Ethernet30/1
   neighbor 172.17.65.107 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.107 remote-as 65113
   neighbor 172.17.65.107 description DC2-POD1-LEAF13B_Ethernet30/1
   neighbor 172.17.65.115 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.115 remote-as 65114
   neighbor 172.17.65.115 description DC2-POD1-LEAF14A_Ethernet30/1
   neighbor 172.17.65.123 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.65.123 remote-as 65114
   neighbor 172.17.65.123 description DC2-POD1-LEAF14B_Ethernet30/1
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family ipv4
      neighbor IPv4-UNDERLAY-PEERS activate
```

# Multicast

# Filters

## Prefix-lists

### Prefix-lists Summary

#### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.4.64.0/24 eq 32 |

### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 10.4.64.0/24 eq 32
```

## Route-maps

### Route-maps Summary

#### RM-CONN-2-BGP

| Sequence | Type | Match and/or Set |
| -------- | ---- | ---------------- |
| 10 | permit | match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |

### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| mgmt | disabled |

## VRF Instances Device Configuration

```eos
!
vrf instance mgmt
```

# Quality Of Service

# EOS CLI

```eos
!
interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB in AMS.yml

```
